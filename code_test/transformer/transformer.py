import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class PositionalEncoding(nn.Module):

    def __init__(self, d_model, max_len=5000):
        """
        d_model:
            embedding维度

        max_len:
            最大序列长度
        """

        super().__init__()


        # 创建一个保存位置编码的矩阵
        # shape:
        # [max_len, d_model]

        pe = torch.zeros(max_len, d_model)


        # position表示token的位置
        # shape:
        # [max_len,1]

        position = torch.arange(
            0,
            max_len
        ).unsqueeze(1)


        # Transformer论文中的公式

        div_term = torch.exp(
            torch.arange(0, d_model, 2)
            *
            (-math.log(10000.0) / d_model)
        )


        # 偶数位置使用sin

        pe[:,0::2] = torch.sin(
            position * div_term
        )


        # 奇数位置使用cos

        pe[:,1::2] = torch.cos(
            position * div_term
        )


        # 增加batch维度

        # [max_len,d_model]
        #
        # 变成
        #
        # [1,max_len,d_model]

        pe = pe.unsqueeze(0)


        # 注册buffer
        # 不参与训练，但是会保存到模型中

        self.register_buffer(
            "pe",
            pe
        )


    def forward(self,x):

        """
        x:
        [batch,seq_len,d_model]

        """

        seq_len = x.size(1)


        # 给embedding加位置

        x = x + self.pe[:,:seq_len]


        return x