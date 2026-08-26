import torch

x = torch.tensor([1.0, 2.0])
print(x.dtype)

y = torch.tensor([1, 2])
print(y.dtype)

z = torch.tensor([1.0, 2.0], dtype=torch.bfloat16)
print(z.dtype)