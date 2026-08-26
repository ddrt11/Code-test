import torch

a = torch.tensor([1, 2, 3])

b = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

c = torch.randn(2, 3, 4)

print(a.shape)
print(b.shape)
print(c.shape)