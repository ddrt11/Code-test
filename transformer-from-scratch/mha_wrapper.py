
import torch
import torch.nn as nn


class MyMHA(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int):
        super().__init__()
       
        # 替换为你阶段5手写MHA代码
        # 下面是临时占位，仅供跑通流程
      
        self.temp_mha = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            batch_first=True
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: [B, T, C]
        return: [B, T, C]
        """
        out, _ = self.temp_mha(x, x, x, need_weights=False)
        return out


if __name__ == "__main__":
    B, T, C = 2, 10, 128
    heads = 8
    mha = MyMHA(hidden_dim=C, num_heads=heads)
    x = torch.randn(B, T, C)
    y = mha(x)
    print(f"6.8 MHA输入 {x.shape},输出 {y.shape}")
    print("="*60)
