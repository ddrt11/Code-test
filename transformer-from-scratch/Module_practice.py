import torch
import torch.nn as nn

class IdentityModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 恒等映射不需要任何可训练参数

    def forward(self, x):
        # 输入什么就返回什么，即恒等映射
        return x


# 运行测试
if __name__ == "__main__":
    model = IdentityModel()
    x = torch.randn(2, 4, 8)  # 任意形状的张量都可以
    
    output = model(x)
    print(f"输入形状: {x.shape}")
    print(f"输出形状: {output.shape}")
    print(f"输入与输出数值完全一致: {torch.equal(x, output)}")
