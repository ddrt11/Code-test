class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j]：word1前i个字符转为word2前j个字符最少操作次数
        dp = [[0]*(n+1) for _ in range(m+1)]

        # 初始化：word1为空，只能不断插入
        for i in range(m+1):
            dp[i][0] = i
        # 初始化：word2为空，只能不断删除
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # 字符相等，不用操作
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 替换、删除、插入 三种操作取最小值 +1
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))
