
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple

# 任务4：MiniGPT.forward(idx, targets=None)
class SingleHeadAttention(nn.Module):
    """单头因果自注意力"""
    def __init__(self, head_size: int, n_embd: int, block_size: int, dropout_p: float):
        super().__init__()
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        # 下三角掩码，不会参与梯度更新
        self.register_buffer("tril_mask", torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)
        # scaled dot product attention
        attn_weight = q @ k.transpose(-2, -1) / (C ** 0.5)
        # 掩盖未来token
        attn_weight = attn_weight.masked_fill(self.tril_mask[:T, :T] == 0, float("-inf"))
        attn_weight = F.softmax(attn_weight, dim=-1)
        attn_weight = self.dropout(attn_weight)
        out = attn_weight @ v
        return out

class MultiHeadAttention(nn.Module):
    """多头自注意力"""
    def __init__(self, num_heads: int, head_size: int, n_embd: int, block_size: int, dropout_p: float):
        super().__init__()
        self.heads = nn.ModuleList([SingleHeadAttention(head_size, n_embd, block_size, dropout_p) for _ in range(num_heads)])
        self.projection = nn.Linear(n_embd, n_embd)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        concat_out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.dropout(self.projection(concat_out))
        return out

class FeedForwardNet(nn.Module):
    def __init__(self, n_embd: int, dropout_p: float):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.GELU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout_p)
        )
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

class TransformerBlock(nn.Module):
    def __init__(self, n_embd: int, n_head: int, block_size: int, dropout_p: float):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size, n_embd, block_size, dropout_p)
        self.ffn = FeedForwardNet(n_embd, dropout_p)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.sa(self.ln1(x))
        x = x + self.ffn(self.ln2(x))
        return x

class MiniGPT(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        n_embd: int,
        block_size: int,
        n_head: int,
        n_layer: int,
        dropout_p: float
    ):
        super().__init__()
        self.block_size = block_size
        self.token_embedding = nn.Embedding(vocab_size, n_embd)
        self.pos_embedding = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[TransformerBlock(n_embd, n_head, block_size, dropout_p) for _ in range(n_layer)])
        self.final_ln = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx: torch.Tensor, targets: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        """
        :param idx: input token id, shape [B, T]
        :param targets: label token id, shape [B, T], None for inference
        :return: logits (B,T,V), loss (scalar or None)
        """
        B, T = idx.shape
        # token embedding + positional embedding
        token_emb = self.token_embedding(idx)
        pos_emb = self.pos_embedding(torch.arange(T, device=idx.device))
        x = token_emb + pos_emb
        x = self.blocks(x)
        x = self.final_ln(x)
        logits = self.lm_head(x)

        loss: Optional[torch.Tensor] = None
        if targets is not None:
            B_dim, T_dim, V_dim = logits.shape
            logits = logits.view(B_dim * T_dim, V_dim)
            targets = targets.view(B_dim * T_dim)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

if __name__ == "__main__":
    model = MiniGPT(vocab_size=64, n_embd=128, block_size=16, n_head=4, n_layer=2, dropout_p=0.1)
    dummy_idx = torch.randint(0, 64, (2, 16))
    logits, loss = model(dummy_idx, dummy_idx)
    print("logits shape:", logits.shape)

