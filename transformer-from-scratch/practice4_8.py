import torch
import torch.nn as nn

if __name__ == "__main__":
    batch, seq_len, d_model = 2, 6, 32
    x = torch.randn(batch, seq_len, d_model)
    w_q = nn.Linear(d_model, d_model)
    w_k = nn.Linear(d_model, d_model)
    w_v = nn.Linear(d_model, d_model)

    Q = w_q(x)
    K = w_k(x)
    V = w_v(x)
    print(f"Q shape {Q.shape}, K shape {K.shape}, V shape {V.shape}")
