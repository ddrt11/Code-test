"""
6.5 和nn.LayerNorm做结果对拍
复制相同参数，对比手写LN与官方LN输出误差
"""
import torch
import torch.nn as nn
from my_layer_norm import MyLayerNorm


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    x = torch.randn(B, T, C)

    my_ln = MyLayerNorm(dim=C, eps=1e-5)
    official_ln = nn.LayerNorm(C, eps=1e-5)

    # 参数拷贝，保证权重完全一样
    official_ln.weight.data.copy_(my_ln.gamma.data)
    official_ln.bias.data.copy_(my_ln.beta.data)

    out_my = my_ln(x)
    out_torch = official_ln(x)

    max_abs_diff = torch.max(torch.abs(out_my - out_torch))
    print(f"6.5 LayerNorm对拍最大误差：{max_abs_diff.item():.3e}")
    print("误差小于1e‑4说明手写实现正确")
    print("="*60)
