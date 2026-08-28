import torch
import torch.nn as nn

class ParamModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 手动建立可训练参数 weight
        self.weight = nn.Parameter(torch.randn(3, 4))  # 自定义张量形状，示例为 3×4


# 实例化模型
model = ParamModel()

# 检查参数是否存在
param_list = list(model.parameters())

print(f"模型可训练参数总数：{len(param_list)}")
print(f"weight 参数形状：{param_list[0].shape}")
print(f"参数是否开启梯度：{param_list[0].requires_grad}")
