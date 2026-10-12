
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    s = Solution()
    nums1 = [3,2,2,3]
    print(s.removeElement(nums1,3))
    nums2 = [0,1,2,2,3,0,4,2]
    print(s.removeElement(nums2,2))
