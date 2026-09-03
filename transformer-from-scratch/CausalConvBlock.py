import torch
import torch.nn as nn

class CausalConvBlock(nn.Module):
    def __init__(self, c, kernel_size=3):
        super().__init__()
        self.kernel_size = kernel_size
        self.pad = kernel_size - 1
        self.conv1d = nn.Conv1d(c, c, kernel_size, padding=self.pad)
        self.ln = nn.LayerNorm(c)

    def forward(self, x):
        # x: [B,T,C] -> conv1d 需要 [B,C,T]
        B, T, C = x.shape
        res = x
        x = self.ln(x)
        x = x.transpose(1,2)
        y = self.conv1d(x)
        # 因果截断，去掉未来padding部分
        y = y[:,:, :-self.pad]
        y = y.transpose(1,2)
        out = res + y
        return out


if __name__ == "__main__":
    B, T, C = 3, 15, 48
    m = CausalConvBlock(C, kernel_size=3)
    x = torch.randn(B,T,C)
    o = m(x)
    print(o.shape)
    o.sum().backward()
    for n,p in m.named_parameters():
        print(n, p.grad is not None)
