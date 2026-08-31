import torch
import torch.nn as nn

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

mlp = TwoLayerMLP(in_d=2, hidden_d=16, out_d=2)
x = torch.randn(5, 2)
out = mlp(x)

print(f"MLP input shape {x.shape}, output shape {out.shape}")
