# [B, T, V] batch_size, sequence_len, vocab_size
# 每一条序列T个token，每个token输出V维vocab logits
# CrossEntropyLoss输入要求是 [N, C]，N是样本数，C类别数
# 所以把B*T个token全部拉平成独立样本
import torch
B, T, V = 2, 4, 100
logits_btv = torch.randn(B, T, V)
print("Original shape [B,T,V]:", logits_btv.shape)
logits_flat = logits_btv.reshape(B * T, V)
print("Flatten shape [B*T,V]:", logits_flat.shape)

labels = torch.randint(0, V, (B, T))
labels_flat = labels.reshape(-1)
print("labels flat shape: ", labels_flat.shape)

# loss = CrossEntropy(logits_flat, labels_flat)
