class CharTokenizer:
    def __init__(self, text: str):
        # 构建词汇表：所有出现过的字符去重并排序
        chars = sorted(list(set(text)))
        self.vocab_size = len(chars)
        
        # 字符 -> 索引 映射
        self.stoi = {ch: i for i, ch in enumerate(chars)}
        # 索引 -> 字符 映射
        self.itos = {i: ch for i, ch in enumerate(chars)}
    
    def encode(self, s: str) -> list[int]:
        """字符串 -> token id 列表"""
        return [self.stoi[c] for c in s]
    
    def decode(self, ids: list[int]) -> str:
        """token id 列表 -> 字符串"""
        return "".join([self.itos[i] for i in ids])


# ========== 测试验证 ==========
if __name__ == "__main__":
    text = "hello transformer"
    tokenizer = CharTokenizer(text)

    s = "hello"
    assert tokenizer.decode(tokenizer.encode(s)) == s
    print("encode('hello'):", tokenizer.encode("hello"))
    print("vocab_size:", tokenizer.vocab_size)
    print("编解码一致性验证通过")
