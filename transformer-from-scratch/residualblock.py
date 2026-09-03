import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.linear1 = nn.Linear(hidden_dim, hidden_dim * 2)
        self.linear2 = nn.Linear(hidden_dim * 2, hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)

    def forward(self, x):
        # x: [B, T, C]
        residual = x
        h = self.norm(x)
        h = self.linear1(h)
        h = torch.relu(h)
        h = self.linear2(h)
        out = residual + h
        return out


# 测试代码
if __name__ == "__main__":
    B, T, C = 2, 10, 32
    model = ResidualBlock(C)
    x = torch.randn(B, T, C, requires_grad=True)
    out = model(x)
    print(f"in shape: {x.shape}")
    print(f"out shape: {out.shape}")
    out.sum().backward()
    # 验证参数有梯度
    for name, param in model.named_parameters():
        print(f"{name} grad exists: {param.grad is not None}")
