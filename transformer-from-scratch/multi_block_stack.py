"""
6.11 堆叠多个 TransformerBlock
用nn.Sequential组装多层block，构成完整Transformer编码器栈

"""
import torch
import torch.nn as nn
from transformer_block import TransformerBlock


class TransformerStack(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, num_layers: int):
        super().__init__()
        block_list = []
        for _ in range(num_layers):
            block_list.append(TransformerBlock(hidden_dim, num_heads))
        self.blocks = nn.Sequential(*block_list)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 顺序经过每一个TransformerBlock
        return self.blocks(x)


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    n_heads = 8
    n_layers = 3  # 堆叠3个block

    stack = TransformerStack(hidden_dim=C, num_heads=n_heads, num_layers=n_layers)
    x = torch.randn(B, T, C)
    output = stack(x)
    print(f"6.11 堆叠{n_layers}层Block，输出shape {output.shape}")
    print("="*60)
