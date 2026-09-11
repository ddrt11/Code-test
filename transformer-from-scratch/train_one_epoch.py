import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from mask_builder import combine_decoder_mask
from teacher_forcing_shift_right import split_teacher_forcing_pair

def train_one_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_fn: nn.CrossEntropyLoss,
    pad_idx: int,
    device: torch.device,
    grad_clip_norm: float = 1.0
) -> float:
    model.train()
    total_loss = 0.0
    total_tokens = 0
    for batch, lengths in dataloader:
        batch = batch.to(device)
        # Teacher forcing shift right
        dec_input, target_label = split_teacher_forcing_pair(batch)
        # build mask
        dec_mask = combine_decoder_mask(dec_input, pad_idx).to(device)
        optimizer.zero_grad(set_to_none=True)
        logits = model(dec_input, dec_mask) # [B, T, V]
        # flatten [B,T,V] -> [B*T, V]
        B, T, V = logits.shape
        logits_flat = logits.reshape(B * T, V)
        labels_flat = target_label.reshape(-1)
        # 只计算非padding token的loss
        non_pad = labels_flat != pad_idx
        loss = loss_fn(logits_flat[non_pad], labels_flat[non_pad])
        loss.backward()
        # gradient clip
        nn.utils.clip_grad_norm_(model.parameters(), max_norm=grad_clip_norm)
        optimizer.step()

        token_count = non_pad.sum().item()
        total_loss += loss.item() * token_count
        total_tokens += token_count
    avg_loss = total_loss / total_tokens
    return avg_loss
