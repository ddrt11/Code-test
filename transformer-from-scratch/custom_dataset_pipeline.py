import torch
from torch.utils.data import Dataset, DataLoader
import random


class TimeSeriesDataset(Dataset):
    """
    变长时序数据集：样本序列长度不统一，需要自定义collate做padding
    模拟：输入一段时间序列，预测未来1个值
    """
    def __init__(self, num_samples=1000, max_len=50):
        self.samples = []
        for _ in range(num_samples):
            # 每个样本随机序列长度 [10, max_len]
            seq_len = random.randint(10, max_len)
            seq = torch.randn(seq_len)
            label = torch.tensor([seq.sum()])
            self.samples.append((seq, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        seq, label = self.samples[idx]
        return seq, label


def collate_fn_pad(batch):
    """
    自定义collate：对不等长序列做padding，返回padding后的tensor + 真实长度mask
    batch: list of (seq, label)
    """
    seqs = [item[0] for item in batch]
    labels = torch.stack([item[1] for item in batch])
    # 获取每个序列真实长度
    lengths = torch.tensor([len(s) for s in seqs])
    # pad到本batch内最长序列
    padded_seqs = torch.nn.utils.rnn.pad_sequence(seqs, batch_first=True, padding_value=0.0)
    # 生成mask：True代表有效位置，False代表pad填充位置
    batch_size, max_seq_len = padded_seqs.shape
    mask = torch.zeros((batch_size, max_seq_len), dtype=torch.bool)
    for i, l in enumerate(lengths):
        mask[i, :l] = True
    return padded_seqs, labels, mask, lengths


if __name__ == "__main__":
    ds = TimeSeriesDataset(num_samples=200)
    loader = DataLoader(ds, batch_size=16, shuffle=True, collate_fn=collate_fn_pad)
    for batch_idx, (p_seq, lab, mask, lens) in enumerate(loader):
        print(f"batch {batch_idx}")
        print(f"padded seq shape: {p_seq.shape}")
        print(f"mask shape: {mask.shape}")
        print(f"real lengths: {lens.tolist()[:5]} ...")
        if batch_idx >= 2:
            break
