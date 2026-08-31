import torch

# y = x^2，对比自动微分与手算梯度
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.pow(x, 2)
loss = y.sum()

loss.backward()

print("==== Practice3.1 y=x^2 梯度验证 ====")
print(f"PyTorch自动梯度 x.grad: {x.grad}")
print(f"手算理论梯度 dy/dx = 2x: {2 * x.detach()}")
