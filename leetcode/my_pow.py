class Solution:
    def myPow(self, x, n):
        # 负指数转换为正指数计算，x取倒数
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        # 快速幂迭代
        while n > 0:
            # n为奇数时，把当前x乘到结果里
            if n % 2 == 1:
                res *= x
            # x平方，指数减半
            x *= x
            n = n // 2
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))
