import torch
import torch.nn as nn

class SelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        b, s, d = x.shape
        Q = self.w_q(x)
        K = self.w_k(x)
        V = self.w_v(x)
        d_k = Q.size(-1)
        scores = Q @ K.transpose(-2,-1) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
        if mask is not None:
            scores = scores.masked_fill(mask, -1e9)
        attn_w = torch.softmax(scores, dim=-1)
        out = attn_w @ V
        return out, attn_w

if __name__ == "__main__":
    model = SelfAttention(d_model=32)
    x = torch.randn(2, 5, 32)
    o, w = model(x)
    print("output shape", o.shape)
