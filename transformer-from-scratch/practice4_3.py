import torch

if __name__ == "__main__":
    batch_size = 2
    seq_len = 5
    d_k = 16
    Q = torch.randn(batch_size, seq_len, d_k)
    K = torch.randn(batch_size, seq_len, d_k)
    V = torch.randn(batch_size, seq_len, d_k)

    attn_score = Q @ K.T
    # scaling
    attn_score = attn_score / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    print("scaled attention score shape:", attn_score.shape)
