
import torch
import torch.nn as nn
import torch.nn.functional as F
from char_tokenizer import CharTokenizer

# 任务2：train / val split
def split_train_validation(token_ids: torch.Tensor, split_ratio: float = 0.9):
    """
    将一维token序列切分为训练集与验证集
    :param token_ids: 完整文本token序列，shape [N]get_batch.py
    :param split_ratio: 训练集占比，默认0.9
    :return: train_data, val_data
    """
    assert 0.0 < split_ratio < 1.0, "划分比例必须在0~1之间"
    total_len = token_ids.shape[0]
    split_point = int(total_len * split_ratio)
    train_data = token_ids[:split_point]
    val_data = token_ids[split_point:]
    return train_data, val_data


if __name__ == "__main__":
    # 假设已经加载文本+tokenizer
    raw_text = "abcdefghijklmnopqrstuvwxyz"
    tokenizer = CharTokenizer(raw_text)
    full_data = torch.tensor(tokenizer.encode(raw_text), dtype=torch.long)
    train_data, val_data = split_train_validation(full_data, 0.9)
    print(f"train len: {len(train_data)}, val len: {len(val_data)}")
