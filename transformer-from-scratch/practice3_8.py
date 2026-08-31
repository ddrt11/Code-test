import torch
import torch.nn as nn
import torch.optim as optim

x = torch.randn(60, 4)
y = torch.where(x[:,0]+x[:,1]>0, torch.tensor(1), torch.tensor(0))

model = nn.Linear(4, 2)
loss_fn = nn.CrossEntropyLoss()
opt = optim.SGD(model.parameters(), lr=0.08)

for e in range(1,101):
    logits = model(x)
    loss = loss_fn(logits, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

    if e % 20 == 0:
        pred = torch.argmax(logits, dim=1)
        acc = (pred == y).float().mean()
        print(f"epoch{e:3d} loss:{loss.item():.4f} acc:{acc.item():.3f}")
