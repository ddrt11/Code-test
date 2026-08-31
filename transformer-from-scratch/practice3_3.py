import torch


batch_size, in_dim, out_dim = 4, 3, 2
x = torch.randn(batch_size, in_dim)
W = torch.randn(in_dim, out_dim, requires_grad=True)
b = torch.randn(out_dim, requires_grad=True)

y = x @ W + b

print(f"输入x shape: {x.shape}")
print(f"W shape: {W.shape}, b shape:{b.shape}")
print(f"输出y shape: {y.shape}")
