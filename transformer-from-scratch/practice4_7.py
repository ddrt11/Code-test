import torch

def create_causal_mask(seq_len):
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
    return mask

def scaled_dot_product_causal(Q,K,V):
    d_k = Q.size(-1)
    scores = Q @ K.transpose(-2,-1) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    s_len = Q.size(-2)
    cmask = create_causal_mask(s_len)
    scores = scores.masked_fill(cmask, -1e9)
    attn_w = torch.softmax(scores, dim=-1)
    out = attn_w @ V
    return out, attn_w

if __name__ == "__main__":
    b, s, d = 1, 5, 8
    qkv = torch.randn(b, s, d)
    out, w = scaled_dot_product_causal(qkv,qkv,qkv)
    print("causal attn weight\n", w[0])
