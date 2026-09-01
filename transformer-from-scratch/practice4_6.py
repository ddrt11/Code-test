import torch

def create_padding_mask(seq, pad_token=0):
    # seq: [batch, seq_len]
    mask = (seq == pad_token).unsqueeze(1).unsqueeze(2)
    return mask # [B, 1, 1, seq_len]

def scaled_dot_product_pad_mask(Q,K,V,pad_mask):
    d_k = Q.size(-1)
    scores = Q @ K.transpose(-2,-1) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    # padding位置设置 -inf
    scores = scores.masked_fill(pad_mask, -1e9)
    attn_w = torch.softmax(scores, dim=-1)
    out = attn_w @ V
    return out, attn_w

if __name__ == "__main__":
    batch = 2
    seq_len = 7
    input_ids = torch.tensor([[1,2,3,4,0,0,0], [5,6,0,0,0,0,0]])
    mask = create_padding_mask(input_ids)
    qkv = torch.randn(batch, seq_len, 16)
    out, w = scaled_dot_product_pad_mask(qkv,qkv,qkv,mask)
    print("padding mask shape", mask.shape)
