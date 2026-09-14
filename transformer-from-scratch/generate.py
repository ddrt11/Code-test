
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List
from minigpt_forward import MiniGPT

# 任务7：generate() 自回归生成函数
@torch.no_grad()
def generate(
    model: MiniGPT,
    idx: torch.Tensor,
    max_new_tokens: int,
    temperature: float = 1.0
) -> torch.Tensor:
    """
    自回归采样生成文本
    :param model: MiniGPT模型实例
    :param idx: 初始上下文token，shape [B, T]
    :param max_new_tokens: 生成token数量
    :param temperature: 温度系数，越小越确定，越大越随机
    :return: idx: [B, T + max_new_tokens]
    """
    model.eval()
    for _ in range(max_new_tokens):
        # 截断上下文，不超过block_size
        context = idx[:, -model.block_size:]
        logits, _ = model(context)
        # 取最后一个位置logits
        logits = logits[:, -1, :]
        # 温度缩放
        logits = logits / temperature
        prob = F.softmax(logits, dim=-1)
        # 多项式采样
        next_token = torch.multinomial(prob, num_samples=1)
        idx = torch.cat([idx, next_token], dim=1)
    return idx

# 本地自测代码
if __name__ == "__main__":
    dev = torch.device("cpu")
    model = MiniGPT(vocab_size=64, n_embd=128, block_size=16, n_head=4, n_layer=2, dropout_p=0.1).to(dev)
    start_ctx = torch.zeros((1,1), dtype=torch.long, device=dev)
    output_ids = generate(model, start_ctx, max_new_tokens=100, temperature=0.8)
    print(output_ids.shape)
