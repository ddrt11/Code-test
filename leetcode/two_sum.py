class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target-n], i]
            d[n] = i

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([3,2,4],6))
    print(s.twoSum([3,3],6))
