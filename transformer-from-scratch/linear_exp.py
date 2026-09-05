"""
6.1 Linear(C,4C) 张量实验
验证 [B,T,C] 输入经过 nn.Linear(C,4*C) 的维度变化
"""
import torch
import torch.nn as nn

if __name__ == "__main__":
    # 超参
    C = 128      # 隐层维度
    B = 2        # batch size
    T = 10       # 序列长度

    # 构造输入张量，形状 [batch, seq_len, hidden_dim]
    x = torch.randn(B, T, C)
    print(f"6.1 输入张量 shape: {x.shape}")

    # 线性层：C映射到4C，FFN的升维操作
    linear_layer = nn.Linear(C, 4 * C)
    output = linear_layer(x)

    print(f"6.1 经过Linear(C,4C)输出 shape: {output.shape}")
    print("="*60)
