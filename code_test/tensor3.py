import torch
import torch.nn as nn
import torch.nn.functional as F


# 参数
batch_size = 2
seq_len = 4
vocab_size = 10000
embedding_dim = 8

num_heads = 2
head_dim = 4


# token
tokens = torch.tensor([
    [23,56,789,100],
    [23,67,890,345]
])


# embedding
embedding = nn.Embedding(
    vocab_size,
    embedding_dim
)

x = embedding(tokens)

print("Embedding:")
print(x.shape)


# QKV
Wq = nn.Linear(
    embedding_dim,
    embedding_dim
)

Wk = nn.Linear(
    embedding_dim,
    embedding_dim
)

Wv = nn.Linear(
    embedding_dim,
    embedding_dim
)


Q = Wq(x)
K = Wk(x)
V = Wv(x)


# split heads

Q = Q.reshape(
    batch_size,
    seq_len,
    num_heads,
    head_dim
)

K = K.reshape(
    batch_size,
    seq_len,
    num_heads,
    head_dim
)

V = V.reshape(
    batch_size,
    seq_len,
    num_heads,
    head_dim
)


# [B,T,H,D]
# ->
# [B,H,T,D]

Q = Q.permute(0,2,1,3)
K = K.permute(0,2,1,3)
V = V.permute(0,2,1,3)


# Attention

scores = Q @ K.transpose(-2,-1)


scores = scores / (head_dim ** 0.5)


attention_weights = F.softmax(
    scores,
    dim=-1
)


output = attention_weights @ V


# merge heads

output = output.permute(
    0,2,1,3
)


output = output.reshape(
    batch_size,
    seq_len,
    embedding_dim
)


print("Attention output:")
print(output.shape)