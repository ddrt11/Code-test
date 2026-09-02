import torch
import torch.nn as nn
from EncoderLayer import EncoderLayer

class Encoder(nn.Module):
    def __init__(self, d_model, n_head, d_ff, num_layers, dropout=0.1):
        super().__init__()
        self.layers = nn.ModuleList([
            EncoderLayer(d_model, n_head, d_ff, dropout)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x, src_mask=None):
        for layer in self.layers:
            x = layer(x, src_mask)
        return self.norm(x)

if __name__ == "__main__":
    B, L, D = 2, 12, 128
    x = torch.randn(B, L, D)
    encoder = Encoder(d_model=128, n_head=4, d_ff=256, num_layers=3)
    enc_out = encoder(x)
    print(f"5.2 encoder output {enc_out.shape}")
