"""
6.3 FeedForward 类
两层线性：C →4C(GELU) →C
依赖：6_2_gelu.py中的gelu函数
"""
import torch
import torch.nn as nn
from gelu import gelu  # 导入gelu函数


class FeedForward(nn.Module):
    def __init__(self, hidden_dim: int):
        super().__init__()
        # w1：升维 C -> 4C
        self.w1 = nn.Linear(hidden_dim, 4 * hidden_dim)
        # w2：降维 4C -> C
        self.w2 = nn.Linear(4 * hidden_dim, hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: [B, T, C]
        return: [B, T, C]
        """
        x = self.w1(x)     # 升维
        x = gelu(x)        # gelu激活
        x = self.w2(x)     # 降维回原维度
        return x


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    ff = FeedForward(hidden_dim=C)
    x_in = torch.randn(B, T, C)
    out = ff(x_in)
    print(f"6.3 FeedForward输入shape {x_in.shape}")
    print(f"6.3 FeedForward输出shape {out.shape}")
    print("="*60)
