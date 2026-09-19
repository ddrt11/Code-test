import torch
import torch.nn as nn
from encoder_block import EncoderBlock
from decoder_block import DecoderBlock

class PosEnc(nn.Module):
    def __init__(self, d_model, max_len=500, drop=0.1):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:,0::2] = torch.sin(pos * div_term)
        pe[:,1::2] = torch.cos(pos * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        seq_len = x.size(1)
        x = x + self.pe[:,:seq_len,:]
        return self.drop(x)


class Transformer(nn.Module):
    def __init__(self, src_vocab, tgt_vocab, d_model, n_head, d_hidden, n_layer, drop=0.1):
        super().__init__()
        self.d_model = d_model
        self.src_emb = nn.Embedding(src_vocab, d_model)
        self.tgt_emb = nn.Embedding(tgt_vocab, d_model)
        self.pos_enc = PosEnc(d_model)

        self.enc_stack = nn.ModuleList([EncoderBlock(d_model, n_head, d_hidden, drop) for _ in range(n_layer)])
        self.dec_stack = nn.ModuleList([DecoderBlock(d_model, n_head, d_hidden, drop) for _ in range(n_layer)])

        self.proj = nn.Linear(d_model, tgt_vocab)

    def forward(self, src_token, tgt_token, src_mask=None, tgt_mask=None):
        # encoder
        x = self.src_emb(src_token)
        x = self.pos_enc(x)
        for block in self.enc_stack:
            x = block(x, src_mask)
        enc_out = x

        # decoder
        y = self.tgt_emb(tgt_token)
        y = self.pos_enc(y)
        for block in self.dec_stack:
            y = block(y, enc_out, tgt_mask, src_mask)
        logits = self.proj(y)
        return logits


def causal_mask(seq_len):
    return torch.tril(torch.ones(seq_len, seq_len)).unsqueeze(0)

if __name__ == "__main__":
    src_vocab = 1000
    tgt_vocab = 1000
    model = Transformer(src_vocab, tgt_vocab, d_model=64, n_head=8, d_hidden=256, n_layer=3)

    bsz = 2
    src = torch.randint(0, src_vocab, (bsz, 10))
    tgt = torch.randint(0, tgt_vocab, (bsz, 6))
    tgt_mask = causal_mask(tgt.size(1))

    logits = model(src, tgt, tgt_mask=tgt_mask)
    print("final logits shape:", logits.shape)
