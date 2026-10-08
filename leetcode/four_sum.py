class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = n-1
                while l < r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l +=1
                        while l<r and nums[r]==nums[r-1]:
                            r -=1
                        l +=1
                        r -=1
                    elif total < target:
                        l +=1
                    else:
                        r -=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))
    print(s.fourSum([2,2,2,2,2], 8))
