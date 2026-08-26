import torch
import torch.nn as nn
import torch.nn.functional as F

class SingleHeadSelfAttention(nn.Module):
    def __init__(self,embed_dim):
        super().__init__()
        #在__init__中定义所有可学习参数
        self.W_q = nn.Linear(embed_dim, embed_dim,bias=False)
        self.W_k = nn.Linear(embed_dim, embed_dim,bias=False)
        self.W_v = nn.Linear(embed_dim, embed_dim,bias=False)
        self.scale = embed_dim ** -0.5

    def forward(self, x):
        #在forward中写计算逻辑
        #x shape: (batch_size, seq_len, embed_dim)
        Q = self.W_q(x)  # shape: (batch_size, seq_len, embed_dim)
        K = self.W_k(x)  # shape: (batch_size, seq_len, embed_dim)
        V = self.W_v(x)  # shape: (batch_size, seq_len, embed_dim)

        #计算注意力分数
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale
        attn_weights = F.softmax(attn_scores, dim=-1)  # shape: (batch_size, seq_len, seq_len)

        #计算加权和
        output = torch.matmul(attn_weights, V)  # shape: (batch_size, seq_len, embed_dim)
        return output
    
#使用
attn = SingleHeadSelfAttention(embed_dim=64)
x = torch.randn(2,10,64)
out = attn(x)
print(out.shape)