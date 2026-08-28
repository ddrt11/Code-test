import torch

# 定义自变量 x，开启梯度追踪
x = torch.tensor(3.0, requires_grad=True)

# 计算 y = x²
y = x ** 2

# 执行反向传播，自动计算梯度
y.backward()

# 观察 x 的梯度
print(f"x.grad = {x.grad}")
