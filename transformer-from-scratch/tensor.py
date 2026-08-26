import torch
import torch.nn as nn

x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print(x.shape)  # Output: torch.Size([2, 3])