"""
6.9 TransformerBlock 完整Pre‑Norm块
组合：LN1 + MHA +残差； LN2 + FFN +残差

"""
import torch
import torch.nn as nn
from my_layer_norm import MyLayerNorm
from mha_wrapper import MyMHA
from feedforward import FeedForward


class TransformerBlock(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int):
        super().__init__()
        self.ln1 = MyLayerNorm(hidden_dim)
        self.mha = MyMHA(hidden_dim, num_heads)
        self.ln2 = MyLayerNorm(hidden_dim)
        self.ffn = FeedForward(hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Pre-Norm完整数据流
        x -> LN1 -> MHA -> +x
        x -> LN2 -> FFN -> +x
        """
        # 注意力子层 +残差
        x = x + self.mha(self.ln1(x))
        # FFN子层 +残差
        x = x + self.ffn(self.ln2(x))
        return x


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    n_heads = 8
    block = TransformerBlock(hidden_dim=C, num_heads=n_heads)
    x_in = torch.randn(B, T, C)
    out = block(x_in)
    print(f"6.9 TransformerBlock输入 {x_in.shape},输出 {out.shape}")
    print("="*60)
