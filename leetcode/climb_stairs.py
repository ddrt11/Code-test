
class Solution:
    def climbStairs(self, n):
        # dp[i] 代表爬到第i阶台阶的方法数
        # 递推公式 dp[i] = dp[i-1] + dp[i-2]
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
