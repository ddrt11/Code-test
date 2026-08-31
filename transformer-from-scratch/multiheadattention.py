import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, num_heads):
        super().__init__()

        assert d_model % num_heads == 0

        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)

        self.Wo = nn.Linear(d_model, d_model)

    def forward(self, X, mask=None):

        B, S, D = X.shape

        Q = self.Wq(X)
        K = self.Wk(X)
        V = self.Wv(X)

        Q = Q.view(B, S, self.num_heads, self.head_dim)
        K = K.view(B, S, self.num_heads, self.head_dim)
        V = V.view(B, S, self.num_heads, self.head_dim)

        Q = Q.transpose(1, 2)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)

        scores = Q @ K.transpose(-2, -1)

        scores = scores / math.sqrt(self.head_dim)

        if mask is not None:
            scores = scores.masked_fill(
                mask == 0,
                float("-inf")
            )

        attention = torch.softmax(scores, dim=-1)

        output = attention @ V

        output = output.transpose(1, 2).contiguous()

        output = output.view(B, S, D)

        output = self.Wo(output)

        return output