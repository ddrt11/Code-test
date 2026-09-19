
import torch
import torch.nn as nn
import torch.nn.functional as F

def scaled_attn(q, k, v, mask=None):
    dk = q.size(-1)
    attn_score = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(torch.tensor(dk, dtype=torch.float32))
    if mask is not None:
        attn_score = attn_score.masked_fill(mask == 0, -1e9)
    attn_w = F.softmax(attn_score, dim=-1)
    out = torch.matmul(attn_w, v)
    return out, attn_w


class MHA(nn.Module):
    def __init__(self, d_model, n_head, drop=0.1):
        super().__init__()
        assert d_model % n_head == 0
        self.d_model = d_model
        self.n_head = n_head
        self.dk = d_model // n_head

        self.wq = nn.Linear(d_model, d_model)
        self.wk = nn.Linear(d_model, d_model)
        self.wv = nn.Linear(d_model, d_model)
        self.wo = nn.Linear(d_model, d_model)
        self.drop = nn.Dropout(drop)

    def split(self, x):
        bsz, seq_len, _ = x.shape
        return x.view(bsz, seq_len, self.n_head, self.dk).transpose(1,2)

    def forward(self, q, k, v, mask=None):
        bsz = q.shape[0]
        q = self.split(self.wq(q))
        k = self.split(self.wk(k))
        v = self.split(self.wv(v))

        attn_out, attn_w = scaled_attn(q, k, v, mask)
        attn_out = attn_out.transpose(1,2).contiguous().view(bsz, -1, self.d_model)
        out = self.drop(self.wo(attn_out))
        return out, attn_w


class FFN(nn.Module):
    def __init__(self, d_model, d_hidden, drop=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_hidden),
            nn.ReLU(),
            nn.Dropout(drop),
            nn.Linear(d_hidden, d_model),
            nn.Dropout(drop)
        )
    def forward(self, x):
        return self.net(x)


class EncoderBlock(nn.Module):
    def __init__(self, d_model, n_head, d_hidden, drop=0.1):
        super().__init__()
        self.mha = MHA(d_model, n_head, drop)
        self.ffn = FFN(d_model, d_hidden, drop)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.drop1 = nn.Dropout(drop)
        self.drop2 = nn.Dropout(drop)

    def forward(self, x, pad_mask=None):
        # Post-LN
        attn_out, _ = self.mha(x, x, x, pad_mask)
        x = self.norm1(x + self.drop1(attn_out))

        ffn_out = self.ffn(x)
        x = self.norm2(x + self.drop2(ffn_out))
        return x


if __name__ == "__main__":
    bsz = 2
    seq_len = 8
    d_model = 64
    n_head = 8
    d_hidden = 256

    block = EncoderBlock(d_model, n_head, d_hidden)
    x = torch.randn(bsz, seq_len, d_model)
    # 构造padding mask示例
    pad_mask = torch.ones(bsz, 1, seq_len, seq_len)
    pad_mask[:, :, 6:, :] = 0

    y = block(x, pad_mask)
    print("encoder block output shape:", y.shape)
