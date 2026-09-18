import torch
from tokenizer import CharTokenizer
from model import MiniGPT

# 超参（和训练保持一致）
batch_size = 32
block_size = 128
n_embd = 192
n_heads = 3
n_layers = 3
dropout = 0.2
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 加载文本初始化tokenizer
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
tokenizer = CharTokenizer(text)

# 加载模型权重
model = MiniGPT(tokenizer.vocab_size, n_embd, block_size, n_heads, n_layers, dropout, device).to(device)
model.load_state_dict(torch.load("tinygpt.pth", map_location=device))
model.eval()

# 输入prompt
prompt = "Once upon a time"
context = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long, device=device)

# 生成500 token
gen_tokens = model.generate(context, max_new_tokens=500, temperature=0.8)
output_text = tokenizer.decode(gen_tokens[0].tolist())
print(output_text)