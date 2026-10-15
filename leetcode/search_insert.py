class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        # 二分查找
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 循环结束时left就是目标的插入位置
        return left

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
