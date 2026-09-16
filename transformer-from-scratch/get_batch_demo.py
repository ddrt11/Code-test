import torch

def get_batch(data: torch.Tensor, batch_size: int, block_size: int):
    """
    从一维 data 中随机抽取 batch 个样本
    返回 x: [batch_size, block_size]
    返回 y: [batch_size, block_size]  （y 是 x 向右错一位）
    """
    # 随机生成 batch_size 个起始位置（保证不越界）
    ix = torch.randint(len(data) - block_size, (batch_size,))
    
    # 每个起始位置取 block_size+1 个 token，前 block_size 是 x，后 block_size 是 y
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+1+block_size] for i in ix])
    return x, y


# ========== 测试验证 ==========
if __name__ == "__main__":
    data = torch.arange(30)
    batch_size = 4
    block_size = 5

    x, y = get_batch(data, batch_size, block_size)
    print("x.shape:", x.shape)  # [4, 5]
    print("y.shape:", y.shape)  # [4, 5]

    # 验证错位关系：每一行的 y[:-1] == x[1:]
    for i in range(batch_size):
        assert torch.equal(y[i, :-1], x[i, 1:])
    print("X/Y 错位关系验证通过")
