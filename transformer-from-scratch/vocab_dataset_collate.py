from torch.utils.data import Dataset, DataLoader
import torch
from collections import Counter

class Vocabulary:
    def __init__(self, special_tokens: dict = None):
        self.stoi = {}
        self.itos = []
        # 特殊token
        self.special = special_tokens or {"<PAD>":0, "<SOS>":1, "<EOS>":2, "<UNK>":3}
        for tok, idx in self.special.items():
            self.stoi[tok] = idx
            self.itos.append(tok)

    def build_vocab(self, corpus:list[str], min_freq:int=2):
        counter = Counter()
        for line in corpus:
            counter.update(line.strip().split())
        for word, cnt in counter.items():
            if cnt >= min_freq and word not in self.stoi:
                self.stoi[word] = len(self.itos)
                self.itos.append(word)
    
    def encode(self, text:str, add_sos_eos=True) -> list[int]:
        tokens = text.strip().split()
        ids = [self.stoi.get(tok, self.stoi["<UNK>"]) for tok in tokens]
        if add_sos_eos:
            ids = [self.stoi["<SOS>"]] + ids + [self.stoi["<EOS>"]]
        return ids
    
    def decode(self, ids:list[int]) -> str:
        tokens = [self.itos[i] for i in ids if i not in set(self.special.values())]
        return " ".join(tokens)
    
    def __len__(self):
        return len(self.itos)

class SeqDataset(Dataset):
    def __init__(self, raw_texts:list[str], vocab:Vocabulary):
        self.raw = raw_texts
        self.vocab = vocab
    
    def __len__(self):
        return len(self.raw)
    
    def __getitem__(self, idx):
        text = self.raw[idx]
        token_ids = self.vocab.encode(text)
        return torch.tensor(token_ids, dtype=torch.long)

def collate_fn(batch:list[torch.Tensor], pad_idx:int):
    """动态padding，返回batch张量 + 序列长度列表"""
    lengths = [x.size(0) for x in batch]
    max_len = max(lengths)
    padded_batch = torch.full((len(batch), max_len), fill_value=pad_idx, dtype=torch.long)
    for i, seq in enumerate(batch):
        padded_batch[i, :seq.size(0)] = seq
    return padded_batch, torch.tensor(lengths)

# Demo使用
if __name__ == "__main__":
    raw_corpus = ["i love deep learning", "transformer is powerful", "pytorch coding practice"]
    vocab = Vocabulary()
    vocab.build_vocab(raw_corpus, min_freq=1)
    ds = SeqDataset(raw_corpus, vocab)
    loader = DataLoader(ds, batch_size=2, shuffle=True, collate_fn=lambda b: collate_fn(b, vocab.stoi["<PAD>"]))
    for batch, lens in loader:
        print(batch.shape, lens)
