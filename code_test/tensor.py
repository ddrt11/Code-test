import torch

# 1. 创建一个包含 1~6 的 Tensor
x = torch.tensor([1, 2, 3, 4, 5, 6])

# 2. 创建一个 2×3 的全 0 Tensor
zeros = torch.zeros(2, 3)

# 3. 创建一个 3×4 的全 1 Tensor
ones = torch.ones(3, 4)

# 4. 创建一个 2×5 的随机 Tensor
random = torch.rand(2, 5)

print(x)
print(zeros)
print(ones)
print(random)

