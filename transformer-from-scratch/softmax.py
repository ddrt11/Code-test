import torch
import torch.nn.functional as F

def my_softmax(x, dim):
    # 数值稳定：减去维度上最大值，不改变softmax输出
    x_max = x.max(dim=dim, keepdim=True)[0]
    exp_x = torch.exp(x - x_max)
    sum_exp_x = exp_x.sum(dim=dim, keepdim=True)
    return exp_x / sum_exp_x


# 测试
x = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])

# 手写softmax，按行dim=1
out_my = my_softmax(x, dim=1)
# 官方F.softmax
out_lib = F.softmax(x, dim=1)

print("手写softmax结果：\n", out_my)
print("官方F.softmax结果：\n", out_lib)
print("是否近似相等：", torch.allclose(out_my, out_lib))

# 验证：每一行求和≈1
print("每行求和：", out_my.sum(dim=1))
