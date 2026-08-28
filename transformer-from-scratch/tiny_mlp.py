import torch
import torch.nn as nn
import torch.optim as optim


class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # 第一层线性层
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        # ReLU 激活函数
        self.relu = nn.ReLU()
        # 第二层线性层
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # 前向传播链路：Linear → ReLU → Linear
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


if __name__ == "__main__":
    # ========== 1. 数据准备 ==========
    batch_size = 8
    input_dim = 10   # 输入特征维度
    hidden_dim = 16  # 隐藏层维度
    output_dim = 5   # 输出类别数

    # 随机生成输入张量与分类标签
    x = torch.randn(batch_size, input_dim)
    target = torch.randint(0, output_dim, (batch_size,))

    # ========== 2. 模型、损失、优化器初始化 ==========
    model = MLP(input_dim, hidden_dim, output_dim)
    criterion = nn.CrossEntropyLoss()       # 分类损失函数
    optimizer = optim.SGD(model.parameters(), lr=0.01)  # SGD 优化器

    # ========== 3. 训练循环 ==========
    epochs = 20
    for epoch in range(epochs):
        # 清零上一轮累计的梯度
        optimizer.zero_grad()

        # 前向传播 forward
        outputs = model(x)

        # 计算损失 loss
        loss = criterion(outputs, target)

        # 反向传播 backward
        loss.backward()

        # 优化器更新参数
        optimizer.step()

        # 打印训练进度
        print(f"Epoch [{epoch+1}/{epochs}] | Loss: {loss.item():.4f}")

    print("\n训练流程结束")
