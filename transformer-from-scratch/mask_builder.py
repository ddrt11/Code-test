import torch

def create_padding_mask(token_ids:torch.Tensor, pad_idx:int) -> torch.Tensor:
    """
    token_ids: [B, T]
    return padding_mask [B, 1, T] 布尔mask，True代表pad位置，要mask掉
    """
    return (token_ids == pad_idx).unsqueeze(1)

def create_causal_mask(seq_len:int, device:torch.device) -> torch.Tensor:
    """
    Causal mask (look ahead mask) [1, seq_len, seq_len]
    True = 需要mask（未来位置不能看）
    上三角为True，对角线及下三角False
    """
    mask = torch.triu(torch.ones((seq_len, seq_len), dtype=torch.bool, device=device), diagonal=1)
    return mask.unsqueeze(0)

def combine_decoder_mask(token_ids:torch.Tensor, pad_idx:int):
    """合并padding mask + causal mask，用于decoder自注意力"""
    B, T = token_ids.shape
    pad_mask = create_padding_mask(token_ids, pad_idx)  # [B,1,T]
    cau_mask = create_causal_mask(T, token_ids.device)  # [1,T,T]
    # broadcast合并，任意一个mask为True就屏蔽
    full_mask = torch.logical_or(pad_mask, cau_mask)
    return full_mask

if __name__ == "__main__":
    t = torch.tensor([[1,4,5,2,0,0], [1,6,2,0,0,0]])
    mask = combine_decoder_mask(t, pad_idx=0)
    print(mask.shape) # [B, T, T]
