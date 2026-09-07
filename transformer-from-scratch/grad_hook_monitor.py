import torch
import torch.nn as nn


class SimpleMLP(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, out_dim)
        self.act = nn.ReLU()

    def forward(self, x):
        x = self.act(self.fc1(x))
        x = self.act(self.fc2(x))
        x = self.fc3(x)
        return x


if __name__ == "__main__":
    model = SimpleMLP(in_dim=16, hidden_dim=128, out_dim=2)
    grad_records = dict()  # 用来保存每层权重梯度norm

    def grad_hook_fn(module, grad_input, grad_output):
        """注册反向传播钩子，每次反向后调用"""
        # 只记录该模块权重的梯度，如果有权重参数
        if hasattr(module, "weight") and module.weight is not None and module.weight.grad is not None:
            grad_norm = torch.norm(module.weight.grad).item()
            grad_records[module._get_name()] = grad_norm
            # 简单检测梯度异常
            if grad_norm > 10:
                print(f"⚠️梯度爆炸警告 {module._get_name()}, grad norm={grad_norm:.4f}")
            if grad_norm < 1e-6:
                print(f"⚠️梯度消失警告 {module._get_name()}, grad norm={grad_norm:.4f}")

    # 给所有线性层注册钩子
    for m in model.modules():
        if isinstance(m, nn.Linear):
            m.register_backward_hook(grad_hook_fn)

    # 模拟一批数据
    x = torch.randn(32, 16)
    y_true = torch.randint(0, 2, (32,))
    logits = model(x)
    loss = nn.CrossEntropyLoss()(logits, y_true)
    loss.backward()

    print("====各层梯度L2范数====")
    for name, g_norm in grad_records.items():
        print(f"{name:10s} | grad norm: {g_norm:.6f}")
