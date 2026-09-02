import torch

def create_causal_mask(seq_len):
    """ 上三角mask，禁止看到未来位置 [1, seq_len, seq_len] """
    mask = torch.tril(torch.ones((seq_len, seq_len), dtype=torch.bool))
    return mask.unsqueeze(0)

def combine_mask(pad_mask, causal_mask):
    """ pad_mask [B,1,1,L], causal_mask [1,Lt,Lt]
    返回合并mask [B,1,Lt,Lt]
    """
    return pad_mask & causal_mask

if __name__ == "__main__":
    L = 6
    causal = create_causal_mask(L)
    print("5.6 causal mask")
    print(causal)
