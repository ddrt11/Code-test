class Solution:
    def searchRange(self, nums, target):
        # 寻找目标值的左边界
        def find_left():
            left = 0
            right = len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # 继续向左搜索，找更靠前的位置
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        
        # 寻找目标值的右边界
        def find_right():
            left = 0
            right = len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # 继续向右搜索，找更靠后的位置
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        
        left_idx = find_left()
        right_idx = find_right()
        return [left_idx, right_idx]

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))
    print(s.searchRange([], 0))
