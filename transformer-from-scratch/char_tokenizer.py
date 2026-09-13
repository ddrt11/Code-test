# 前置环境
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List

# 任务1：CharTokenizer encode() / decode()
class CharTokenizer:
    """字符级Tokenizer，字符与token id双向映射"""
    def __init__(self, raw_text: str):
        # 提取所有唯一字符并排序
        unique_chars = sorted(list(set(raw_text)))
        self.vocab_size = len(unique_chars)
        # 双向映射字典
        self.char_to_idx = {char: idx for idx, char in enumerate(unique_chars)}
        self.idx_to_char = {idx: char for idx, char in enumerate(unique_chars)}

    def encode(self, input_str: str) -> List[int]:
        """字符串 -> token id列表"""
        token_ids = []
        for c in input_str:
            if c not in self.char_to_idx:
                raise KeyError(f"字符 `{c}` 不在词表内")
            token_ids.append(self.char_to_idx[c])
        return token_ids

    def decode(self, token_ids: List[int]) -> str:
        """token id列表 -> 原始字符串"""
        chars = []
        for tid in token_ids:
            if tid not in self.idx_to_char:
                raise KeyError(f"token id `{tid}` 不在词表内")
            chars.append(self.idx_to_char[tid])
        return "".join(chars)


if __name__ == "__main__":
    test_text = "hello world"
    tokenizer = CharTokenizer(test_text)
    ids = tokenizer.encode("hello")
    print("encode result:", ids)
    print("decode result:", tokenizer.decode(ids))
