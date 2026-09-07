import torch
import torch.nn as nn
import torch.optim as optim
from torch.cuda.amp import autocast, GradScaler


class ConvToy(nn.Module):
    """简单卷积网络，演示混合精度"""
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(64, 5)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = self.pool(x).flatten(1)
        return self.fc(x)


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ConvToy().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    scaler = GradScaler()  # fp16混合精度缩放器

    num_step = 10
    for step in range(num_step):
        batch_img = torch.randn(16, 3, 32, 32).to(device)
        batch_label = torch.randint(0,5,(16,)).to(device)

        optimizer.zero_grad(set_to_none=True)

        # autocast上下文：前向使用半精度加速
        with autocast(dtype=torch.float16):
            logits = model(batch_img)
            loss = criterion(logits, batch_label)

        # 缩放loss，反向传播，防止fp16下梯度下溢
        scaler.scale(loss).backward()

        # 梯度裁剪，防止梯度爆炸
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        scaler.step(optimizer)
        scaler.update()  # 更新缩放因子

        if (step+1) % 2 ==0:
            print(f"step {step+1:2d} | loss:{loss.item():.4f}")

    print("混合精度训练循环结束")
