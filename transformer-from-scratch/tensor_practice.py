import torch

# 定义维度参数
B, T, C = 4, 8, 16
H, D = 4, 4  # 必须满足 H * D = C，才可进行reshape拆分

# 1. 随机生成形状为 [B, T, C] 的张量
x = torch.randn(B, T, C)
print(f"初始形状 [B,T,C]: {x.shape}")

# 2. 重塑为 [B, T, H, D]（将特征维度C拆分为H和D）
x_btHD = x.reshape(B, T, H, D)
print(f"第一步 [B,T,H,D]: {x_btHD.shape}")

# 3. 维度置换为 [B, H, T, D]（交换 T 与 H 两个维度）
x_bHTD = x_btHD.permute(0, 2, 1, 3)
print(f"第二步 [B,H,T,D]: {x_bHTD.shape}")

# 4. 置换回 [B, T, H, D]（再次交换 T 与 H 维度）
x_btHD_back = x_bHTD.permute(0, 2, 1, 3)
print(f"第三步 [B,T,H,D]: {x_btHD_back.shape}")

# 5. 重塑回 [B, T, C]（将H和D合并回特征维度C）
x_final = x_btHD_back.reshape(B, T, C)
print(f"最终形状 [B,T,C]: {x_final.shape}")

# 验证：整个过程仅改变张量视图，数值完全一致
print(f"数值一致性验证: {torch.allclose(x, x_final)}")
