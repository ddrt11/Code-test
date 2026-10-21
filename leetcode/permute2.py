class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # 先排序，方便识别重复元素
        n = len(nums)
        used = [False] * n
        
        def backtrack(path):
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                # 跳过同层重复元素：前一个元素和当前相同，且前一个未被使用
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1,1,2]))
    print(s.permuteUnique([1,2,3]))
