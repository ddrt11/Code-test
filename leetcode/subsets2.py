class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()  # 先排序，方便后续去重
        
        # 回溯：start起始下标，path当前子集
        def backtrack(start, path):
            res.append(path.copy())
            for i in range(start, len(nums)):
                # 同层跳过重复元素，避免生成重复子集
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # 回溯
        
        backtrack(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))
    print(s.subsetsWithDup([0]))
