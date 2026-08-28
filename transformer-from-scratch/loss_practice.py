import torch
import torch.nn as nn

# 1. 准备数据
logits = torch.randn(4, 10)  # 形状 [4, 10]：4个样本，每个样本对应10个类别的未归一化预测分数
target = torch.randint(0, 10, (4,))  # 形状 [4]：4个样本的真实类别标签，取值范围 0~9

# 2. 计算分类损失（交叉熵损失）
criterion = nn.CrossEntropyLoss()
loss = criterion(logits, target)

print(f"logits 形状: {logits.shape}")
print(f"target 形状: {target.shape}")
print(f"分类损失值: {loss.item():.4f}")
