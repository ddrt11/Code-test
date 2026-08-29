# layers.py
import torch
import torch.nn as nn
import torch.nn.functional as F


class MyLinear(nn.Module):
    """手写线性层，等价nn.Linear"""
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_features, in_features))
        self.bias = nn.Parameter(torch.zeros(out_features))

    def forward(self, x):
        # x: [..., in_features]
        return x @ self.weight.T + self.bias


class MyEmbedding(nn.Module):
    """手写Embedding查表"""
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(vocab_size, embedding_dim))

    def forward(self, token_ids):
        # token_ids [B,T] → output [B,T,C]
        return self.weight[token_ids]


class MyLayerNorm(nn.Module):
    """手写LayerNorm，对最后一维归一化"""
    def __init__(self, feature_dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.gamma = nn.Parameter(torch.ones(feature_dim))
        self.beta = nn.Parameter(torch.zeros(feature_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta


class MySoftmax(nn.Module):
    """手写Softmax，带数值稳定"""
    def __init__(self):
        super().__init__()

    def forward(self, x, dim):
        x_max = x.max(dim=dim, keepdim=True)[0]
        exp_x = torch.exp(x - x_max)
        sum_exp = exp_x.sum(dim=dim, keepdim=True)
        return exp_x / sum_exp
