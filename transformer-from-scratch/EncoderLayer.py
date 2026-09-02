import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_head):
        super().__init__()
        assert d_model % n_head == 0
        self.d_k = d_model // n_head
        self.n_head = n_head
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        B, Lq, _ = q.shape
        B, Lk, _ = k.shape
        q = self.w_q(q).view(B, Lq, self.n_head, self.d_k).transpose(1,2)
        k = self.w_k(k).view(B, Lk, self.n_head, self.d_k).transpose(1,2)
        v = self.w_v(v).view(B, Lk, self.n_head, self.d_k).transpose(1,2)
        attn_score = torch.matmul(q, k.transpose(-1,-2)) / torch.sqrt(torch.tensor(self.d_k, dtype=torch.float32))
        if mask is not None:
            attn_score = attn_score.masked_fill(mask == 0, -1e9)
        attn_weight = F.softmax(attn_score, dim=-1)
        out = torch.matmul(attn_weight, v)
        out = out.transpose(1,2).contiguous().view(B, Lq, -1)
        return self.w_o(out)

class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model)
        )
    def forward(self, x):
        return self.net(x)

class EncoderLayer(nn.Module):
    def __init__(self, d_model, n_head, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_head)
        self.ffn = FeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.drop1 = nn.Dropout(dropout)
        self.drop2 = nn.Dropout(dropout)

    def forward(self, x, src_mask=None):
        attn_out = self.self_attn(x, x, x, mask=src_mask)
        x = self.norm1(x + self.drop1(attn_out))
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.drop2(ffn_out))
        return x

# 测试
if __name__ == "__main__":
    B, L, D = 2, 10, 128
    x = torch.randn(B, L, D)
    layer = EncoderLayer(d_model=128, n_head=4, d_ff=256)
    out = layer(x)
    print(f"5.1 output shape {out.shape}") # [B,L,D]
