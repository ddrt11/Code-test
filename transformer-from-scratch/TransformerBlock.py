import torch
import torch.nn as nn

class Attention(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.qkv = nn.Linear(embed_dim, embed_dim * 3)
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        B, T, C = x.shape
        qkv = self.qkv(x).split(C, dim=-1)
        q, k, v = qkv
        attn_score = q @ k.transpose(-2, -1) / (C ** 0.5)
        mask = torch.tril(torch.ones(T, T))
        attn_score = attn_score.masked_fill(mask == 0, float("-inf"))
        attn_weight = torch.softmax(attn_score, dim=-1)
        out = attn_weight @ v
        return self.out_proj(out)


class FeedForward(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, 4 * embed_dim),
            nn.GELU(),
            nn.Linear(4 * embed_dim, embed_dim)
        )

    def forward(self, x):
        return self.net(x)



class TransformerBlock(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attn = Attention(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.ffn = FeedForward(embed_dim)

    def forward(self, x):
        # pre‑norm + 残差连接
        x = x + self.attn(self.norm1(x))
        x = x + self.ffn(self.norm2(x))
        return x


# 测试
if __name__ == "__main__":
    C = 128
    block = TransformerBlock(C)
    x = torch.randn(2, 10, C)
    out = block(x)
    print(f"输入 {x.shape} → 输出 {out.shape}")
