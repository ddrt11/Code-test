"""
6.10 forward + backward完整测试
跑前向传播，执行backward，验证梯度链路正常，无None梯度
"""
import torch
from transformer_block import TransformerBlock


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    n_heads = 8

    block = TransformerBlock(hidden_dim=C, num_heads=n_heads)
    # requires_grad=True，开启张量梯度计算
    x = torch.randn(B, T, C, requires_grad=True)

    # --------前向传播--------
    y = block(x)
    print(f"6.10 forward输出 shape: {y.shape}")

    # --------反向传播--------
    loss = y.sum()
    loss.backward()

    # 判断梯度是否生成成功
    grad_valid = x.grad is not None
    print(f"6.10 backward测试，梯度有效：{grad_valid}")
    print("="*60)
