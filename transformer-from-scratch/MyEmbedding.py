import torch
import torch.nn as nn

class MyEmbedding(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        # 构造可训练的词表权重，等价nn.Embedding内部weight
        self.weight = nn.Parameter(torch.randn(vocab_size, embedding_dim))

    def forward(self, token_ids):
        # tensor索引查表：[B,T] → [B,T,C]
        return self.weight[token_ids]


B, T = 2, 4
vocab_size = 100
C = 8

# 实例化手写版本
my_emb = MyEmbedding(vocab_size, C)
# 官方embedding
official_emb = nn.Embedding(vocab_size, C)

# 为了对比，把官方权重赋值给手写，保证权重完全一样
my_emb.weight.data.copy_(official_emb.weight.data)

token_ids = torch.randint(0, vocab_size, (B, T))

out1 = my_emb(token_ids)
out2 = official_emb(token_ids)

print("手写输出shape:", out1.shape)   # [2,4,8]
print("官方输出shape:", out2.shape)   # [2,4,8]
print("两者数值是否全部相等：", torch.allclose(out1, out2))
