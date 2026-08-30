import torch
import torch.nn as nn
import torch.nn.functional as F

class SingleHeadSelfAttention(nn.Module):
    def __init__(self, in_dim, head_dim):
        super().__init__()
        self.wq = nn.Linear(in_dim, head_dim)
        self.wk = nn.Linear(in_dim, head_dim)
        self.wv = nn.Linear(in_dim, head_dim)
        self.scale = head_dim ** 0.5

    def forward(self, x):
        B, T, C = x.shape          # x.shape [B, T, C] = [2, 5, 16]
        q = self.wq(x)             # q.shape [B, T, head_dim] = [2, 5, 8]
        k = self.wk(x)             # k.shape [B, T, head_dim] = [2, 5, 8]
        v = self.wv(x)             # v.shape [B, T, head_dim] = [2, 5, 8]

        # Q @ K^T
        attn_scores = torch.matmul(q, k.transpose(-2, -1))  # [B, T, T] = [2, 5, 5]
        attn_scores = attn_scores / self.scale              # [B, T, T] = [2, 5, 5]
        attn_weights = F.softmax(attn_scores, dim=-1)       # [B, T, T] = [2, 5, 5]

        out = torch.matmul(attn_weights, v)                 # [B, T, head_dim] = [2, 5, 8]
        return out

B = 2
T = 5
C = 16
head_dim = 8

model = SingleHeadSelfAttention(in_dim=C, head_dim=head_dim)
x = torch.randn(B, T, C)   # [2, 5, 16]
res = model(x)
print(res.shape) # 输出 torch.Size([2, 5, 8])
