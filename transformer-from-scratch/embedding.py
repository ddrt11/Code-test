import torch
import torch.nn as nn

B = 2   # 2条样本
T = 4   # 每条序列4个token
C = 8   # 嵌入维度8

embedding = nn.Embedding(vocab_size=100, embedding_dim=C)
token_ids = torch.randint(0, 100, (B, T))  # shape [2,4]

x = embedding(token_ids)
print(x.shape) # torch.Size([2, 4, 8]) → [B,T,C]
