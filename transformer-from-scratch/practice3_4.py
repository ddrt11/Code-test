import torch

lr = 0.05

x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_true = torch.tensor([[2.5], [4.4], [6.7], [8.3]])

w = torch.randn(1, 1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

for step in range(8):
    y_pred = x @ w + b
    loss = ((y_pred - y_true) ** 2).mean()

    loss.backward()
    # 手动更新参数，脱离计算图
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
    # 梯度清零
    w.grad.zero_()
    b.grad.zero_()

    if step % 2 == 0:
        print(f"step {step}, loss={loss.item():.3f}, w={w.item():.3f}, b={b.item():.3f}")
