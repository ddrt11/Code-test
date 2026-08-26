import torch
import torch.nn as nn

class MultiLayerNet(nn.Module):
    def __init__(self):
        super().__init__()
        #正确使用ModuleList包装
        self.layers = nn.ModuleList([
            nn.Linear(10, 20),
            nn.Linear(20, 20),
            nn.Linear(20, 5)
        ])

    def forward(self, x):
        for layer in self.layers:
            x = torch.relu(layer(x))
        return x