import torch
x = torch.randn(3, 4)

print("shape:", x.shape)
print("ndim:", x.ndim)
print("dtype:", x.dtype)
print("device:", x.device)