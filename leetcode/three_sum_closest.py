class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return closest

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))
    print(s.threeSumClosest([0,0,0], 1))
