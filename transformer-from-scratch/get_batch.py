# 前置环境
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple

# 任务3：get_batch()
def get_batch(
    split: str,
    train_data: torch.Tensor,
    val_data: torch.Tensor,
    block_size: int,
    batch_size: int,
    device: torch.device
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    采样一批训练样本
    x:上下文token，y:目标token（右移一位）
    return: x (B,T), y (B,T)
    """
    assert split in ["train", "val"], "split只能是train或val"
    data = train_data if split == "train" else val_data
    # 随机生成batch_size个合法起始索引
    max_start_pos = len(data) - block_size
    ix = torch.randint(low=0, high=max_start_pos, size=(batch_size,))
    # 批量截取序列
    x = torch.stack([data[i : i + block_size] for i in ix])
    y = torch.stack([data[i+1 : i + block_size + 1] for i in ix])
    # 迁移到目标设备
    x = x.to(device)
    y = y.to(device)
    return x, y


if __name__ == "__main__":
    dev = torch.device("cpu")
    fake_data = torch.arange(100)
    xb, yb = get_batch("train", fake_data, fake_data, block_size=4, batch_size=2, device=dev)
    print("xb shape:", xb.shape, "\nyb shape:", yb.shape)
