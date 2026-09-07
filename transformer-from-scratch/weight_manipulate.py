import torch
import torch.nn as nn
import torch.optim as optim


class DemoNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(32, 128),
            nn.GELU(),
            nn.Linear(128, 128),
            nn.GELU(),
        )
        self.head = nn.Linear(128, 10)

    def forward(self, x):
        x = self.backbone(x)
        return self.head(x)


if __name__ == "__main__":
    model = DemoNet()

    # ==========1.冻结backbone主干，只训练head分类头==========
    for name, param in model.backbone.named_parameters():
        param.requires_grad = False
    print("冻结后需要训练的参数：")
    for n, p in model.named_parameters():
        if p.requires_grad:
            print(f"  {n}")

    # ==========2.参数分组优化器：不同学习率，主干极小lr，头部正常lr==========
    optimizer = optim.AdamW([
        {"params": model.backbone.parameters(), "lr": 1e-5},
        {"params": model.head.parameters(), "lr": 1e-3}
    ], weight_decay=1e-4)

    # ==========3.手动修改某一层权重（简单权重扰动实验）==========
    with torch.no_grad():
        # 给head权重加小噪声
        noise = 0.01 * torch.randn_like(model.head.weight)
        model.head.weight.add_(noise)

    # ==========4.保存部分权重，只保存head，不保存主干==========
    save_dict = {"head_weight": model.head.weight.data,
                 "head_bias": model.head.bias.data,
                 "opt_state": optimizer.state_dict()}
    torch.save(save_dict, "partial_weight.pt")

    # ==========5.模拟加载部分权重==========
    ckpt = torch.load("partial_weight.pt")
    model.head.weight.data.copy_(ckpt["head_weight"])
    model.head.bias.data.copy_(ckpt["head_bias"])

    # 模拟训练一步
    x = torch.randn(8, 32)
    y = torch.randint(0, 10, (8,))
    pred = model(x)
    loss = nn.CrossEntropyLoss()(pred, y)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print("单步训练完成，部分权重读写测试OK")
