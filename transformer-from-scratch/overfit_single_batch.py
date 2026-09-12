import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from mask_builder import combine_decoder_mask
from teacher_forcing_shift_right import split_teacher_forcing_pair
from vocab_dataset_collate import SeqDataset, collate_fn

def overfit_single_batch(model, vocab, pad_idx, device, n_iter=2000, lr=3e-4):
    """只用同一个batch反复训练，看loss收敛到接近0"""
    # 构造固定单条batch数据
    raw_text = ["i love deep learning transformer coding practice"]
    ds = SeqDataset(raw_text, vocab)
    loader = DataLoader(ds, batch_size=1, collate_fn=lambda b: collate_fn(b, pad_idx))
    single_batch = next(iter(loader))
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    batch, _ = single_batch
    batch = batch.to(device)

    for i in range(n_iter):
        dec_input, target_label = split_teacher_forcing_pair(batch)
        dec_mask = combine_decoder_mask(dec_input, pad_idx).to(device)
        logits = model(dec_input, dec_mask)
        B, T, V = logits.shape
        logits_flat = logits.reshape(B*T, V)
        labels_flat = target_label.reshape(-1)
        non_pad = labels_flat != pad_idx
        loss = loss_fn(logits_flat[non_pad], labels_flat[non_pad])

        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        if i % 100 == 0:
            print(f"Iter {i:4d} | Loss: {loss.item():.6f}")
    return model
