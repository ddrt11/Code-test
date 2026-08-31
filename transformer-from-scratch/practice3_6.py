import torch
import torch.nn as nn
import torch.optim as optim


x = torch.rand(100, 1) * 10
y = 3 * x + 2 + 0.2 * torch.randn_like(x)

model = nn.Linear(1, 1)
criterion = nn.MSELoss()
opt = optim.SGD(model.parameters(), lr=0.03)

for epoch in range(300):
    pred = model(x)
    loss = criterion(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

    if epoch % 50 == 0:
        w = model.weight.item()
        b = model.bias.item()
        print(f"epoch {epoch:3d} | loss:{loss.item():.4f} | w={w:.3f} | b={b:.3f}")
