
import torch
import torch.nn as nn
import torch.nn.functional as F

# 任务5：[B,T,V] -> [B*T,V] 的 Cross Entropy
def compute_gpt_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """
    GPT风格交叉熵损失计算
    logits: [B, T, Vocab]
    targets: [B, T]
    return: scalar loss
    """
    B, T, vocab_size = logits.shape
    # 三维展平为二维，适配CrossEntropy输入要求
    logits_flat = logits.reshape(B * T, vocab_size)
    targets_flat = targets.reshape(B * T)
    # 计算交叉熵
    loss = F.cross_entropy(logits_flat, targets_flat)
    return loss


if __name__ == "__main__":
    B, T, V = 2, 4, 10
    logits = torch.randn(B, T, V)
    targets = torch.randint(0, V, (B, T))
    loss_val = compute_gpt_loss(logits, targets)
    print("loss value:", loss_val.item())
