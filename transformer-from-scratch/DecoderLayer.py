import torch
import torch.nn as nn
import torch.nn.functional as F
from EncoderLayer import MultiHeadAttention, FeedForward

class DecoderLayer(nn.Module):
    def __init__(self, d_model, n_head, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_head)
        self.cross_attn = MultiHeadAttention(d_model, n_head)
        self.ffn = FeedForward(d_model, d_ff)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.drop1 = nn.Dropout(dropout)
        self.drop2 = nn.Dropout(dropout)
        self.drop3 = nn.Dropout(dropout)

    def forward(self, tgt, memory, tgt_mask=None, src_tgt_mask=None):
        # Masked self attention
        attn1 = self.self_attn(tgt, tgt, tgt, mask=tgt_mask)
        tgt = self.norm1(tgt + self.drop1(attn1))
        # Cross attention
        attn2 = self.cross_attn(q=tgt, k=memory, v=memory, mask=src_tgt_mask)
        tgt = self.norm2(tgt + self.drop2(attn2))
        # FFN
        ffn_out = self.ffn(tgt)
        tgt = self.norm3(tgt + self.drop3(ffn_out))
        return tgt

if __name__ == "__main__":
    B, Lt, D = 2, 8, 128
    Lm = 10
    tgt = torch.randn(B, Lt, D)
    memory = torch.randn(B, Lm, D)
    dec_layer = DecoderLayer(d_model=128, n_head=4, d_ff=256)
    out = dec_layer(tgt, memory)
    print(f"5.3 decoder layer output {out.shape}")
