"""
6.2 GELU 激活函数实现
Transformer FFN使用GELU，不是ReLU
公式：0.5 * x * (1 + tanh( sqrt(2/π) * (x + 0.044715*x³) ))
"""
import torch

def gelu(x: torch.Tensor) -> torch.Tensor:
    """手写GELU"""
    pi = torch.tensor(torch.pi)
    sqrt_2_over_pi = torch.sqrt(torch.tensor(2.0) / pi)
    term = x + 0.044715 * torch.pow(x, 3)
    return 0.5 * x * (1.0 + torch.tanh(sqrt_2_over_pi * term))


if __name__ == "__main__":
    # 简单测试
    test_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])
    result = gelu(test_tensor)
    print(f"6.2 GELU输入：{test_tensor}")
    print(f"6.2 GELU输出：{result}")
    print("="*60)
