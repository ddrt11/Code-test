import torch
import torch.nn as nn
import torch.optim as optim

class TwoLayerMLP(nn.Module):
    def __init__(self, in_d, hidden_d, out_d):
        super().__init__()
        self.fc1 = nn.Linear(in_d, hidden_d)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_d, out_d)
    def forward(self, x):
        h = self.fc1(x)
        h = self.relu(h)
        out = self.fc2(h)
        return out

mlp = TwoLayerMLP(4, 12, 2)
loss_fn = nn.CrossEntropyLoss()
opt = optim.Adam(mlp.parameters(), lr=1e-2)

x = torch.randn(80,4)
y = torch.where((x[:,0] - x[:,2])>0, torch.tensor(0), torch.tensor(1))
num_epoch = 15

for epoch in range(num_epoch):
    opt.zero_grad()         # 1.梯度清零
    logit = mlp(x)          # 2.前向传播forward
    loss_val = loss_fn(logit, y) #3.计算loss
    loss_val.backward()     #4.反向传播backward
    opt.step()              #5.参数更新step

    print(f"Epoch {epoch+1:2d} | loss={loss_val.item():.4f}")
