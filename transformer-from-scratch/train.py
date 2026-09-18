import torch
from tokenizer import CharTokenizer
from dataset import get_batch
from model import MiniGPT

# 超参
batch_size = 32
block_size = 128
n_embd = 192
n_heads = 3
n_layers = 3
dropout = 0.2
lr = 3e-4
max_iters = 5000
eval_interval = 200
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 读取文本
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
tokenizer = CharTokenizer(text)
data = torch.tensor(tokenizer.encode(text), dtype=torch.long)
split = int(0.9 * len(data))
train_data = data[:split]
val_data = data[split:]

model = MiniGPT(tokenizer.vocab_size, n_embd, block_size, n_heads, n_layers, dropout, device).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split_name in ['train', 'val']:
        losses = torch.zeros(10)
        for k in range(10):
            xb, yb = get_batch(split_name, train_data if split_name=='train' else val_data, block_size, batch_size, device)
            logits, loss = model(xb, yb)
            losses[k] = loss.item()
        out[split_name] = losses.mean()
    model.train()
    return out

# 训练循环
for iter in range(max_iters):
    if iter % eval_interval == 0:
        losses = estimate_loss()
        print(f"iter {iter}, train loss: {losses['train']:.4f}, val loss: {losses['val']:.4f}")
    xb, yb = get_batch('train', train_data, block_size, batch_size, device)
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

# 保存模型
torch.save(model.state_dict(), "tinygpt.pth")
print("Model saved to tinygpt.pth")