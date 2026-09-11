# Teacher Forcing：训练时，decoder输入是目标序列右移(shift right)，用真实token而不是模型上一步预测
# Shift Right: tgt -> decoder_input = tgt[:, :-1], label = tgt[:, 1:]
import torch

def split_teacher_forcing_pair(tgt_batch:torch.Tensor):
    """
    tgt_batch: [B, T] 包含<SOS> ... <EOS>
    return: dec_input(shift right), target_label
    dec_input: 去掉最后一位 [B, T-1]
    target_label: 去掉第一位<SOS> [B, T-1]
    """
    dec_input = tgt_batch[:, :-1]
    target_label = tgt_batch[:, 1:]
    return dec_input, target_label

# Demo
if __name__ == "__main__":
    # batch中2条句子，token id包含SOS, token, EOS
    tgt = torch.tensor([[1, 5, 7, 2, 0], [1, 9, 2, 0, 0]])
    dec_in, label = split_teacher_forcing_pair(tgt)
    print("Shift Right Decoder Input:\n", dec_in)
    print("Ground Truth Label:\n", label)
    # 训练：dec_in送入decoder，预测label，这就是Teacher Forcing
