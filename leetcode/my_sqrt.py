class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找，找最大的mid满足 mid*mid <= x
        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                ans = mid  # 记录这个候选答案
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))
