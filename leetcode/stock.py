class Solution:
    def maxProfit(self, prices):
        min_p = prices[0]
        profit = 0
        for p in prices:
            if p < min_p:
                min_p = p
            else:
                profit = max(profit, p - min_p)
        return profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
