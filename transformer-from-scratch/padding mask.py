import torch

def create_padding_mask(seq, pad_idx=0):
    """ seq: [B, L]  token id序列, pad_idx为padding符号
    返回 mask: [B,1,1,L] 用于multi‑head attention
    True=有效，0=pad位置，会被mask掉
    """
    B, L = seq.shape
    mask = (seq != pad_idx).unsqueeze(1).unsqueeze(2)
    return mask

if __name__ == "__main__":
    src_tokens = torch.tensor([
        [12,34,56,0,0],
        [22,0,0,0,0]
    ])
    pad_mask = create_padding_mask(src_tokens, pad_idx=0)
    print("5.5 Padding Mask")
    print(pad_mask)
    print(pad_mask.shape)
