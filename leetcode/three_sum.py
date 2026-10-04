class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                sm = nums[i]+nums[l]+nums[r]
                if sm ==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l +=1
                    while l<r and nums[r]==nums[r-1]:
                        r -=1
                    l +=1
                    r -=1
                elif sm <0:
                    l +=1
                else:
                    r -=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([0,1,1]))
    print(s.threeSum([0,0,0]))
