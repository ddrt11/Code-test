import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()#必须先调用父类初始化
        self.linear1 = nn.Linear(10, 5)#子模块，内部包含weights和bias

    def forward(self, x):
        #在这里写计算逻辑，支持任意python语法：条件，循环，分支
        x = self.linear1(x)
        x = torch.relu(x)
        return x
    
model = SimpleNet()#实例化模型
x = torch.randn(2, 10)#输入数据
output = model(x)#调用forward方法