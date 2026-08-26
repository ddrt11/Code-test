import torch
#创建一个三维的tensor
#假设：
#B = Batch size = 2
#S = Sequence length = 4
#D = Dimension = 6
x = torch.arange(2*4*6).reshape(2,4,6)

print("原始 Tensor: ")
print(x)

print("\n原始 Tensor 的形状: ")
print(x.shape)

#取第一个Batch

first_batch = x[0]
print("\n第一个 Batch: ")
print(first_batch)

print("\n第一个 Batch 的形状: ")
print(first_batch.shape)

#取所有Batch的第一个Token
first_token_all_batches = x[:,0,:]
print("\n所有 Batch 的第一个 Token: ")
print(first_token_all_batches)

print("\n所有 Batch 的第一个 Token 的形状: ")
print(first_token_all_batches.shape)

#取所有Batch的最后一个Token
last_token_all_batches = x[:,-1,:]
print("\n所有 Batch 的最后一个 Token: ")
print(last_token_all_batches)

print("\n所有 Batch 的最后一个 Token 的形状: ")
print(last_token_all_batches.shape)

#取所有Token的第0个特征
feature_0_all_tokens = x[:,:,0]
print("\n所有 Token 的第0个特征: ")
print(feature_0_all_tokens)

print("\n所有 Token 的第0个特征的形状: ")
print(feature_0_all_tokens.shape)

#取第一个Batch的第一个Token
first_token_first_batch = x[0,0,:]
print("\n第一个 Batch 的第一个 Token: ")
print(first_token_first_batch)

print("\n第一个 Batch 的第一个 Token 的形状: ")
print(first_token_first_batch.shape)

#取一个具体的元素
specific_element = x[1,2,3]
print("\n具体的元素 (Batch 1, Token 2, Feature 3): ")
print(specific_element)

print("\n具体的元素的形状: ")
print(specific_element.shape)
