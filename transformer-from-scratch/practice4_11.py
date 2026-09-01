import torch
import torch.nn as nn

class MyMultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads

        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        b, s, dm = x.shape
        x = x.view(b, s, self.num_heads, self.d_head)
        x = x.transpose(1,2).contiguous()
        return x

    def combine_heads(self, x):
        b, nh, s, dh = x.shape
        x = x.transpose(1,2).contiguous().view(b, s, self.d_model)
        return x

    def forward(self, q_in, k_in, v_in, mask=None):
        b = q_in.size(0)
        Q = self.split_heads(self.w_q(q_in))
        K = self.split_heads(self.w_k(k_in))
        V = self.split_heads(self.w_v(v_in))

        d_k = torch.tensor(self.d_head, dtype=torch.float32)
        scores = Q @ K.transpose(-2,-1) / torch.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask, -1e9)
        attn_w = torch.softmax(scores, dim=-1)
        attn_out = attn_w @ V

        concat = self.combine_heads(attn_out)
        final = self.out_proj(concat)
        return final, attn_w

if __name__ == "__main__":
    mha = MyMultiHeadAttention(d_model=64, num_heads=8)
    x = torch.randn(2, 7, 64)
    out, aw = mha(x,x,x)
    print(f"MHA output shape {out.shape}")
