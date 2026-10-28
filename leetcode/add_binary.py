class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0  # 进位
        i = len(a) - 1
        j = len(b) - 1
        # 两个字符串没遍历完 或者 还有进位时继续循环
        while i >= 0 or j >= 0 or carry > 0:
            # 取出当前位置数字，越界就取0
            num_a = int(a[i]) if i >= 0 else 0
            num_b = int(b[j]) if j >= 0 else 0
            total = num_a + num_b + carry
            carry = total // 2   # 新进位
            res.append(str(total % 2))
            i -= 1
            j -= 1
        # 结果是逆序的，反转拼接
        return "".join(reversed(res))

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
