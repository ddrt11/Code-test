import torch

if __name__ == "__main__":
    batch_size = 2
    seq_len = 5
    d_k = 16
    Q = torch.randn(batch_size, seq_len, d_k)
    K = torch.randn(batch_size, seq_len, d_k)
    attn_score = Q @ K.T / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    attn_weights = torch.softmax(attn_score, dim=-1)
    print("attn_weights shape", attn_weights.shape)
    print("row sum check", attn_weights[0,0].sum())
