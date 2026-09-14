import torch
import torch.nn as nn
import torch.nn.functional as F
from get_batch import get_batch
from minigpt_forward import MiniGPT


# 任务6：完整 training loop
def estimate_validation_loss(model, train_data, val_data, block_size, batch_size, device, eval_steps: int = 200):
    model.eval()
    loss_record = {"train": 0.0, "val":0.0}
    with torch.no_grad():
        for split in ["train", "val"]:
            total_loss = 0.0
            for _ in range(eval_steps):
                x, y = get_batch(split, train_data, val_data, block_size, batch_size, device)
                logits, loss = model(x, y)
                total_loss += loss.item()
            loss_record[split] = total_loss / eval_steps
    model.train()
    return loss_record


def run_training(
    model,
    train_data: torch.Tensor,
    val_data: torch.Tensor,
    block_size: int,
    batch_size: int,
    max_iters: int,
    eval_interval: int,
    lr: float,
    device: torch.device
):
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, betas=(0.9,0.95))
    for step in range(max_iters):
        # 评估
        if step % eval_interval == 0:
            loss_stats = estimate_validation_loss(model, train_data, val_data, block_size, batch_size, device)
            print(f"iter {step:5d} | train_loss: {loss_stats['train']:.4f} | val_loss: {loss_stats['val']:.4f}")
        # 前向反向传播
        xb, yb = get_batch("train", train_data, val_data, block_size, batch_size, device)
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        # 可选梯度裁剪
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
    return model

# 本地自测入口
if __name__ == "__main__":
    dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 超参
    hp = {
        "vocab_size":64,
        "n_embd":128,
        "block_size":16,
        "n_head":4,
        "n_layer":2,
        "dropout_p":0.1
    }
    net = MiniGPT(**hp).to(dev)
    fake_train = torch.randint(0,64,(1000,))
    fake_val = torch.randint(0,64,(200,))
    trained_model = run_training(
        model=net,
        train_data=fake_train,
        val_data=fake_val,
        block_size=16,
        batch_size=16,
        max_iters=1000,
        eval_interval=200,
        lr=3e-4,
        device=dev
    )


