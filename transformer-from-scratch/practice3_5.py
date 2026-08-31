import torch

# 带噪声数据集
x = torch.rand(100, 1) * 10
y = 3 * x + 2 + 0.2 * torch.randn_like(x)

w = torch.randn(1, 1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
lr = 0.03
epochs = 300

for epoch in range(epochs):
    y_pred = x @ w + b
    loss = torch.mean((y_pred - y) ** 2)

    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_()
    b.grad.zero_()

    if epoch % 50 == 0:
        print(f"epoch {epoch:3d} | loss:{loss.item():.4f} | w={w.item():.3f} | b={b.item():.3f}")
