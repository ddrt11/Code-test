import torch

if __name__ == "__main__":
    batch, seq_len, d_model = 2, 8, 64
    num_heads = 8
    d_head = d_model // num_heads
    x = torch.randn(batch, seq_len, d_model)

    # reshape multi‑head
    x = x.view(batch, seq_len, num_heads, d_head)
    x = x.transpose(1, 2)
    x = x.contiguous()
    print(f"after view‑transpose‑contiguous: {x.shape}")

    # 复原
    x = x.transpose(1,2).contiguous().view(batch, seq_len, d_model)
    print(f"recover shape {x.shape}")
