class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        slow = 2
        # fast遍历，slow指向新数组待插入位置
        for fast in range(2, len(nums)):
            # 和新数组倒数第二个不同，即可保留
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == "__main__":
    s = Solution()
    arr1 = [1,1,1,2,2,3]
    print(s.removeDuplicates(arr1), arr1[:5])
    arr2 = [0,0,1,1,1,1,2,3,3]
    print(s.removeDuplicates(arr2), arr2[:7])
