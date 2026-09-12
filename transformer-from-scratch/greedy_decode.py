import torch
import torch.nn as nn
from vocab_dataset_collate import Vocabulary
from mask_builder import combine_decoder_mask

@torch.no_grad()
def greedy_autoregressive_decode(
    device:torch.device,
    pad_idx:int,
    eos_idx:int,
    model:nn.Module,
    vocab:Vocabulary,
    prompt_text:str,
    max_new_tokens:int=40,
    
) -> str:
    model.eval()
    # encode prompt
    prompt_ids = vocab.encode(prompt_text, add_sos_eos=False)
    generated = torch.tensor([[vocab.stoi["<SOS>"]] + prompt_ids], dtype=torch.long, device=device)
    for _ in range(max_new_tokens):
        T = generated.size(1)
        mask = combine_decoder_mask(generated, pad_idx).to(device)
        logits = model(generated, mask) # [1, T, V]
        next_token_logits = logits[:, -1, :] #取最后位置 [1, V]
        next_token_id = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        if next_token_id.item() == eos_idx:
            break
        generated = torch.cat([generated, next_token_id], dim=1)
    # decode
    result_ids = generated[0].cpu().tolist()
    return vocab.decode(result_ids)
