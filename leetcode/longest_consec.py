class Solution:
    def longestConsecutive(self, nums):
        st = set(nums)
        max_len = 0
        for x in st:
            # x-1不在集合里，说明x是一段连续序列的起点
            if x - 1 not in st:
                cur = x
                cnt = 1
                while cur + 1 in st:
                    cur += 1
                    cnt += 1
                max_len = max(max_len, cnt)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,0,1,2]))
