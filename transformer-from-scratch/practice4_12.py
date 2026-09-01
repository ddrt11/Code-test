import torch
import torch.nn as nn

class RewriteMHA(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.dh = d_model // n_heads
        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.o_proj = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        bs = q.shape[0]
        q = self.q_proj(q).view(bs, -1, self.n_heads, self.dh).transpose(1,2)
        k = self.k_proj(k).view(bs, -1, self.n_heads, self.dh).transpose(1,2)
        v = self.v_proj(v).view(bs, -1, self.n_heads, self.dh).transpose(1,2)

        score = torch.matmul(q, k.transpose(-1,-2)) / (self.dh**0.5)
        if mask is not None:
            score = score.masked_fill(mask, -1e9)
        attn = torch.softmax(score, dim=-1)
        val = torch.matmul(attn, v)

        val = val.transpose(1,2).contiguous().view(bs, -1, self.d_model)
        output = self.o_proj(val)
        return output, attn

if __name__ == "__main__":
    model = RewriteMHA(d_model=128, n_heads=16)
    x = torch.randn(3, 10, 128)
    res, a = model(x,x,x)
    print(f"rewrite MHA output shape {res.shape}")
