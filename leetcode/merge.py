class Solution:
    def merge(self, nums1, m, nums2, n):
        # 三个指针：从后往前填充，避免覆盖nums1的有效元素
        i = m - 1    # nums1有效元素末尾
        j = n - 1    # nums2末尾
        k = m + n - 1  # 合并后数组末尾
        
        # 从后往前比较，大的放到k位置
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # nums2还有剩余元素，直接拷贝到nums1前面
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    s.merge(nums1, 3, [2,5,6], 3)
    print(nums1)
