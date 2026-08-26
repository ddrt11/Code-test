import torch

x = torch.tensor([1,5,2,8,3])
mask = x>4

print(mask)  # 输出: tensor([False,  True, False,  True, False])

print(x[mask])  # 输出: tensor([5, 8])
print(x[x>4])  # 输出: tensor([5, 8])