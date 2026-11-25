class Solution:
    def minCut(self, s):
        n = len(s)
        # dp[i]：s[0..i]最少分割次数
        dp = [i for i in range(n)]
        # 预处理回文表
        is_pal = [[False]*n for _ in range(n)]
        for r in range(n):
            for l in range(r+1):
                if s[l]==s[r] and (r-l <= 2 or is_pal[l+1][r-1]):
                    is_pal[l][r] = True
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if is_pal[j+1][i]:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.minCut("aab"))
    print(s.minCut("a"))
    print(s.minCut("ab"))
