import torch
import torch.nn as nn
import torch.nn.functional as F

class CausalSelfAttention(nn.Module):
    def __init__(self, in_dim, head_dim):
        super().__init__()
        self.wq = nn.Linear(in_dim, head_dim)
        self.wk = nn.Linear(in_dim, head_dim)
        self.wv = nn.Linear(in_dim, head_dim)
        self.scale = head_dim ** 0.5

    def forward(self, x):
        B, T, C = x.shape                     # [B, T, C]
        q = self.wq(x)                        # [B, T, head_dim]
        k = self.wk(x)                        # [B, T, head_dim]
        v = self.wv(x)                        # [B, T, head_dim]

        attn_scores = torch.matmul(q, k.transpose(-2, -1))  # [B, T, T]
        attn_scores = attn_scores / self.scale               # [B, T, T]

        # 构造因果掩码: j>i 的位置置为 -inf，softmax之后变成0
        mask = torch.tril(torch.ones(T, T, device=x.device)) # [T, T] 下三角矩阵
        attn_scores = attn_scores.masked_fill(mask == 0, float('-inf')) # [B, T, T]

        attn_weights = F.softmax(attn_scores, dim=-1)        # [B, T, T]，j>i处权重=0
        out = torch.matmul(attn_weights, v)                  # [B, T, head_dim]
        return out, attn_weights

B = 2
T = 5
C = 16
head_dim = 8

model = CausalSelfAttention(in_dim=C, head_dim=head_dim)
x = torch.randn(B, T, C)
output, attn_w = model(x)

# 验证条件：对所有 i, j > i， attn_w[b,i,j] == 0
print("attention weight shape:", attn_w.shape)
print("Attention矩阵（第一个batch）：")
print(attn_w[0])

# 断言测试 j>i 的位置全部为0
for i in range(T):
    for j in range(T):
        if j > i:
            assert torch.allclose(attn_w[:, i, j], torch.zeros_like(attn_w[:, i, j]), atol=1e-6), f"错误位置 i={i},j={j}"
print(" 因果掩码校验通过，j>i位置权重全部为0")
