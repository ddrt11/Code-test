import torch
import torch.nn as nn
import torch.nn.functional as F
from encoder_block import MHA, FFN

def scaled_attn(q, k, v, mask=None):
    dk = q.size(-1)
    attn_score = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(torch.tensor(dk, dtype=torch.float32))
    if mask is not None:
        attn_score = attn_score.masked_fill(mask == 0, -1e9)
    attn_w = F.softmax(attn_score, dim=-1)
    out = torch.matmul(attn_w, v)
    return out, attn_w


class DecoderBlock(nn.Module):
    def __init__(self, d_model, n_head, d_hidden, drop=0.1):
        super().__init__()
        self.mask_mha = MHA(d_model, n_head, drop)
        self.cross_mha = MHA(d_model, n_head, drop)
        self.ffn = FFN(d_model, d_hidden, drop)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.d1 = nn.Dropout(drop)
        self.d2 = nn.Dropout(drop)
        self.d3 = nn.Dropout(drop)

    def forward(self, x, enc_out, tgt_mask=None, cross_mask=None):
        # 1. 带因果mask的目标端自注意力
        attn1, _ = self.mask_mha(x, x, x, tgt_mask)
        x = self.norm1(x + self.d1(attn1))

        # 2. 交叉注意力 query来自decoder, k/v来自encoder
        attn2, _ = self.cross_mha(x, enc_out, enc_out, cross_mask)
        x = self.norm2(x + self.d2(attn2))

        # 3. FFN
        ffn_out = self.ffn(x)
        x = self.norm3(x + self.d3(ffn_out))
        return x


def causal_mask(seq_len):
    # 上三角置0，禁止看到未来token
    mask = torch.tril(torch.ones(seq_len, seq_len))
    return mask.unsqueeze(0)

if __name__ == "__main__":
    bsz = 2
    src_len = 10
    tgt_len = 6
    d_model = 64
    n_head = 8
    d_hidden = 256

    dec_block = DecoderBlock(d_model, n_head, d_hidden)
    x = torch.randn(bsz, tgt_len, d_model)
    enc_out = torch.randn(bsz, src_len, d_model)
    tgt_mask = causal_mask(tgt_len)

    y = dec_block(x, enc_out, tgt_mask)
    print("decoder block output shape:", y.shape)
