"""
6.6 Residual x + F(x) 残差连接演示
残差：输入直接加到子模块输出上，缓解梯度消失
"""
import torch

if __name__ == "__main__":
    B, T, C = 2, 10, 128
    x = torch.randn(B, T, C)   # 原始输入
    Fx = torch.randn_like(x)   # F(x)：网络子模块计算结果

    out = x + Fx   # 残差相加核心代码

    print(f"6.6 原始输入x shape {x.shape}")
    print(f"6.6 子模块输出F(x) shape {Fx.shape}")
    print(f"6.6 残差输出 x+F(x) shape {out.shape}")
    print("="*60)
