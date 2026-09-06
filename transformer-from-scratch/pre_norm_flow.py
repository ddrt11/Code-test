"""
6.7 Pre‑Norm 数据流演示（仅逻辑，不完整网络）
Pre‑Norm范式：先归一化，再送入子模块，再残差相加
数据流顺序：
x → LN1 → MHA → +x → LN2 → FFN → +x
区别于 Post‑Norm：先子模块+残差，再归一化
本文件只展示数据流逻辑，不做完整网络实例化
"""
import torch
import torch.nn as nn
from my_layer_norm import MyLayerNorm
from feedforward import FeedForward


def pre_norm_flow_demo():
    B, T, C = 2, 10, 128
    x = torch.randn(B, T, C)

    ln1 = MyLayerNorm(C)
    ln2 = MyLayerNorm(C)
    ffn = FeedForward(C)

   
    # 注意力子层
    x_norm1 = ln1(x)
    # mha_out = mha(x_norm1)
    mha_out = torch.randn_like(x_norm1)  # 模拟MHA输出
    x = x + mha_out  # 残差

    # FFN子层
    x_norm2 = ln2(x)
    ffn_out = ffn(x_norm2)
    x = x + ffn_out  # 残差
    return x


if __name__ == "__main__":
    res = pre_norm_flow_demo()
    print(f"6.7 Pre‑Norm数据流演示输出shape {res.shape}")
    print("Pre‑Norm：归一化放在子模块之前")
    print("="*60)
