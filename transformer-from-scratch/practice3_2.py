import torch

# y = (3x+2)^2
# 链式求导：dy/dx = 2*(3x+2)*3 = 6*(3x+2)
x = torch.tensor(1.5, requires_grad=True)
z = 3 * x + 2
y = torch.pow(z, 2)

y.backward()

print("==== Practice3.2 链式法则 y=(3x+2)^2 ====")
print(f"PyTorch梯度 x.grad = {x.grad.item():.4f}")
manual_grad = 6 * (3 * 1.5 + 2)
print(f"手算链式法则梯度 = {manual_grad:.4f}")
