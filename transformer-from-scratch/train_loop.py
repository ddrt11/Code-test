import torch
import torch.nn as nn
import torch.nn.functional as F

# ========== 1. CharTokenizer ==========
class CharTokenizer:
    def __init__(self, text):
        chars = sorted(list(set(text)))
        self.vocab_size = len(chars)
        self.stoi = {ch: i for i, ch in enumerate(chars)}
        self.itos = {i: ch for i, ch in enumerate(chars)}
    def encode(self, s):
        return [self.stoi[c] for c in s]
    def decode(self, ids):
        return "".join([self.itos[i] for i in ids])

# ========== 2. get_batch ==========
def get_batch(data, batch_size, block_size):
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+1+block_size] for i in ix])
    return x, y

# ========== 3. MiniGPT ==========
class MiniGPT(nn.Module):
    def __init__(self, vocab_size, block_size, n_embd, n_layer):
        super().__init__()
        self.block_size = block_size
        self.token_embedding = nn.Embedding(vocab_size, n_embd)
        self.position_embedding = nn.Embedding(block_size, n_embd)
        self.transformer_blocks = nn.Sequential(
            *[nn.TransformerEncoderLayer(d_model=n_embd, nhead=2, batch_first=True) 
              for _ in range(n_layer)]
        )
        self.final_norm = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)
    
    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding(idx)
        pos_emb = self.position_embedding(torch.arange(T, device=idx.device))
        x = tok_emb + pos_emb
        x = self.transformer_blocks(x)
        x = self.final_norm(x)
        logits = self.lm_head(x)
        
        loss = None
        if targets is not None:
            B, T, V = logits.shape
            loss = F.cross_entropy(logits.view(B*T, V), targets.view(B*T))
        return logits, loss

# ========== 生成函数 ==========
def generate(model, idx, max_new_tokens):
    model.eval()
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -model.block_size:]
        logits, _ = model(idx_cond)
        logits = logits[:, -1, :]
        idx_next = torch.argmax(logits, dim=-1, keepdim=True)
        idx = torch.cat([idx, idx_next], dim=1)
    return idx


# ========== 训练主程序 ==========
if __name__ == "__main__":
    text = "abcabcabcabcabcabc" * 100
    tokenizer = CharTokenizer(text)
    data = torch.tensor(tokenizer.encode(text), dtype=torch.long)

    # 超参数
    batch_size = 8
    block_size = 8
    n_embd = 32
    n_layer = 2
    learning_rate = 1e-3
    max_steps = 500

    model = MiniGPT(tokenizer.vocab_size, block_size, n_embd, n_layer)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    for step in range(max_steps):
        xb, yb = get_batch(data, batch_size, block_size)
        
        # forward
        logits, loss = model(xb, yb)
        
        # zero grad
        optimizer.zero_grad(set_to_none=True)
        # backward
        loss.backward()
        # update
        optimizer.step()
        
        if step % 100 == 0:
            print(f"step {step:3d} | loss: {loss.item():.4f}")

    # 生成测试
    start = torch.tensor([tokenizer.encode("a")], dtype=torch.long)
    generated = generate(model, start, 20)
    print("\n生成结果:", tokenizer.decode(generated[0].tolist()))
