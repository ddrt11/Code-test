import torch
import torch.nn as nn

class GatedFFN(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.w_gate = nn.Linear(dim, dim)
        self.w_value = nn.Linear(dim, dim)
        self.w_out = nn.Linear(dim, dim)
        self.ln = nn.LayerNorm(dim)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x):
        # x [B, T, C]
        residual = x
        x = self.ln(x)
        gate = torch.sigmoid(self.w_gate(x))
        val = torch.tanh(self.w_value(x))
        hidden = gate * val
        hidden = self.w_out(hidden)
        hidden = self.dropout(hidden)
        out = residual + hidden
        return out


if __name__ == "__main__":
    B, T, C = 2, 12, 64
    net = GatedFFN(C)
    x = torch.randn(B, T, C)
    out = net(x)
    print(out.shape)
    out.sum().backward()
    for n,p in net.named_parameters():
        print(n, p.grad is not None)
