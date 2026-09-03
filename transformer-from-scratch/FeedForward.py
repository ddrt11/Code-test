import torch
import torch.nn as nn

class FeedForward(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, 4 * embed_dim),
            nn.GELU(),
            nn.Linear(4 * embed_dim, embed_dim)
        )

    def forward(self, x):
        return self.net(x)


# 测试代码
if __name__ == "__main__":
    C = 128
    ff = FeedForward(C)
    # batch=2, seq_len=10, channel=C
    x = torch.randn(2, 10, C)
    out = ff(x)
    print(f"输入shape: {x.shape}")
    print(f"输出shape: {out.shape}")
