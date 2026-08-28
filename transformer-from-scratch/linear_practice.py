import torch
import torch.nn as nn

class MyLinear(nn.Module):
    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        super().__init__()
        # 手动定义可训练参数 W 和 b，形状与官方 nn.Linear 对齐
        self.W = nn.Parameter(torch.empty(out_features, in_features))
        if bias:
            self.b = nn.Parameter(torch.empty(out_features))
        else:
            self.register_parameter('b', None)
        
        # 与官方一致的参数初始化方式
        nn.init.kaiming_uniform_(self.W, a=5 ** 0.5)
        if self.b is not None:
            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(self.W)
            bound = 1 / fan_in ** 0.5
            nn.init.uniform_(self.b, -bound, bound)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 核心公式 Y = XW + b
        # x 形状: [..., in_features]
        # W.T 形状: [in_features, out_features]
        out = x @ self.W.T
        if self.b is not None:
            out = out + self.b
        return out


if __name__ == "__main__":
    torch.manual_seed(0)
    
    # 初始化官方层与自定义层
    official_layer = nn.Linear(8, 16)
    my_layer = MyLinear(8, 16)
    
    # 同步两者参数，保证输入条件完全一致
    my_layer.W.data = official_layer.weight.data.clone()
    my_layer.b.data = official_layer.bias.data.clone()
    
    # 构造题目中的输入张量
    x = torch.randn(2, 4, 8)
    
    out_official = official_layer(x)
    out_my = my_layer(x)
    
    print(f"官方输出形状：{out_official.shape}")
    print(f"自定义输出形状：{out_my.shape}")
    print(f"数值一致性验证：{torch.allclose(out_official, out_my, atol=1e-6)}")
