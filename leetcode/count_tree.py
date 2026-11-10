
class Solution:
    def numTrees(self, n):
        # dp[i]：i个节点的二叉搜索树一共有多少种
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # j作为根，左边j-1个节点，右边i-j个节点
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
