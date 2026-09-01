import torch

# Q: 3x2
Q = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0]])
K = torch.tensor([[0.5, 1.0],
                  [1.5, 2.0]])

n_rows_q = Q.shape[0]
n_cols_k = K.shape[1]
n_inner = Q.shape[1]

result = torch.zeros((n_rows_q, n_cols_k))
# 手动循环实现 Q @ K.T
for i in range(n_rows_q):
    for j in range(n_cols_k):
        s = 0.0
        for k_idx in range(n_inner):
            s += Q[i, k_idx] * K[j, k_idx]
        result[i, j] = s

print("手动计算 QK^T:\n", result)
print("shape:", result.shape)
