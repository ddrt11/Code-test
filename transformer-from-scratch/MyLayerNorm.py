import torch
import torch.nn as nn

class MyLayerNorm(nn.Module):
    def __init__(self, feature_dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        # gamma 缩放、beta偏移，可训练参数，shape等于特征维度
        self.gamma = nn.Parameter(torch.ones(feature_dim))
        self.beta = nn.Parameter(torch.zeros(feature_dim))

    def forward(self, x):
        # 在最后一维计算均值、方差 keepdim保持维度方便广播
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        # 标准化
        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        # gamma缩放 + beta偏移
        out = self.gamma * x_norm + self.beta
        return out


# 测试对比官方nn.LayerNorm
B, T, C = 2, 3, 4  # [B,T,C]
x = torch.randn(B, T, C)

my_ln = MyLayerNorm(feature_dim=C)
official_ln = nn.LayerNorm(normalized_shape=C, eps=1e-5)

# 复制权重，保证两者参数一致
my_ln.gamma.data.copy_(official_ln.weight.data)
my_ln.beta.data.copy_(official_ln.bias.data)

out_my = my_ln(x)
out_off = official_ln(x)

print("手写LN shape", out_my.shape)
print("官方LN shape", out_off.shape)
print("结果是否接近：", torch.allclose(out_my, out_off))
