import torch
import torch.nn as nn
import torch.nn.functional as F

class SingleHeadSelfAttention(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        # Q K V 投影矩阵
        self.w_q = nn.Linear(in_dim, out_dim)
        self.w_k = nn.Linear(in_dim, out_dim)
        self.w_v = nn.Linear(in_dim, out_dim)
        self.scale = out_dim ** 0.5

    def forward(self, x):
        B, T, C = x.shape
        # 得到 Q K V: [B, T, D]
        q = self.w_q(x)
        k = self.w_k(x)
        v = self.w_v(x)

        # 注意力分数 Q @ K^T  [B, T, T]
        attn_score = torch.matmul(q, k.transpose(-2, -1)) / self.scale
        attn_weight = F.softmax(attn_score, dim=-1)

        # 和V相乘得到输出 [B,T,D]
        out = torch.matmul(attn_weight, v)
        return out
