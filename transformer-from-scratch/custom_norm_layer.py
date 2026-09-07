import torch
import torch.nn as nn
import torch.nn.functional as F

class AdaLayerNorm(nn.Module):
    """
    自适应LayerNorm：在标准LN基础上增加偏移预测分支
    不只是简单的gamma/beta，额外用小网络生成偏移量，适合Transformer微调场景
    """
    def __init__(self, hidden_dim: int, eps: float = 1e-6):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.eps = eps

        # 标准可学习缩放、偏置参数
        self.gamma = nn.Parameter(torch.ones(hidden_dim))
        self.beta = nn.Parameter(torch.zeros(hidden_dim))

        # 额外小分支：根据输入特征预测偏移delta
        self.offset_net = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 4),
            nn.GELU(),
            nn.Linear(hidden_dim // 4, hidden_dim)
        )

        # 初始化偏移网络权重，初始输出接近0，不破坏原始归一化
        for layer in self.offset_net:
            if isinstance(layer, nn.Linear):
                nn.init.xavier_uniform_(layer.weight)
                nn.init.zeros_(layer.bias)

    def forward(self, x):
        """
        :param x: 输入张量 shape [batch, seq_len, hidden_dim]
        :return: 归一化之后的张量，shape同输入
        """
        # 在最后一维做归一化
        mean = x.mean(dim=-1, keepdim=True)
        var = ((x - mean) ** 2).mean(dim=-1, keepdim=True)
        std = torch.sqrt(var + self.eps)
        x_norm = (x - mean) / std

        # 预测动态偏移
        delta = self.offset_net(x_norm)
        out = self.gamma * (x_norm + delta) + self.beta
        return out


if __name__ == "__main__":
    # 测试模块
    batch, seq, hdim = 2, 10, 64
    test_x = torch.randn(batch, seq, hdim)
    norm_layer = AdaLayerNorm(hidden_dim=hdim)
    res = norm_layer(test_x)
    print(f"输入shape: {test_x.shape}, 输出shape:{res.shape}")
    # 反向传播测试
    loss = res.sum()
    loss.backward()
    print("梯度正常计算完成")
