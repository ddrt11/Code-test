import torch

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.size(-1)
    attn_scores = Q @ K.transpose(-2, -1) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    attn_weights = torch.softmax(attn_scores, dim=-1)
    output = attn_weights @ V
    return output, attn_weights

if __name__ == "__main__":
    b, s, d = 2, 6, 12
    q = torch.randn(b, s, d)
    k = torch.randn(b, s, d)
    v = torch.randn(b, s, d)
    out, w = scaled_dot_product_attention(q,k,v)
    print(f"out shape {out.shape}")
