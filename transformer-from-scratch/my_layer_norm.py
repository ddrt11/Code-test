"""
6.4 手写LayerNorm
对最后一维做归一化，带可学习gamma、beta参数
"""
import torch
import torch.nn as nn


class MyLayerNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        # gamma 缩放，初始全1
        self.gamma = nn.Parameter(torch.ones(dim))
        # beta 偏移，初始全0
        self.beta = nn.Parameter(torch.zeros(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: [B, T, C]
        在最后一维做归一化
        unbiased=False：和pytorch官方LN保持方差计算一致
        keepdim=True：保留维度，方便广播
        """
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        out = self.gamma * x_norm + self.beta
        return out


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    my_ln = MyLayerNorm(dim=C)
    x = torch.randn(B, T, C)
    y = my_ln(x)
    print(f"6.4 MyLayerNorm输入 {x.shape},输出 {y.shape}")
    print("="*60)
