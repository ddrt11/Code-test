import torch

def dot_product_attention_raw(Q, K, V):
    attn_score = Q @ K.T
    attn_weight = torch.softmax(attn_score, dim=-1)
    out = attn_weight @ V
    return out, attn_weight

if __name__ == "__main__":
    batch_size = 1
    seq_len = 4
    d_model = 8
    Q = torch.randn(batch_size, seq_len, d_model)
    K = torch.randn(batch_size, seq_len, d_model)
    V = torch.randn(batch_size, seq_len, d_model)
    output, attn = dot_product_attention_raw(Q, K, V)
    print(f"output shape {output.shape}")
