import torch
import torch.nn.functional as F

if __name__ == "__main__":
    B = 4
    T = 8
    V = 20

    # 模拟模型输出和标签
    logits = torch.randn(B, T, V)    # [B, T, V]
    targets = torch.randint(0, V, (B, T))  # [B, T]

    # 形状转换：展平 batch 和时间维度
    logits_flat = logits.view(B * T, V)    # [B*T, V]
    targets_flat = targets.view(B * T)     # [B*T]

    # 计算交叉熵损失
    loss = F.cross_entropy(logits_flat, targets_flat)
    print("loss:", loss.item())

    print(f"\nB={B}, T={T}")
    print(f"一次forward总共 {B*T} 次分类，每次是 {V} 分类问题")
