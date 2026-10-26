class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            # 以当前元素结尾的最大子数组和：要么重新开始，要么接上之前的子数组
            cur = max(nums[i], cur + nums[i])
            # 更新全局最大值
            max_sum = max(max_sum, cur)
        return max_sum

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))
