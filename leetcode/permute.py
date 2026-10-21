class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)
        used = [False] * n  # 标记数字是否已经被选入当前排列
        
        def backtrack(path):
            # 当前路径长度等于数组长度，得到一个完整排列
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False
        
        backtrack([])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([0,1]))
    print(s.permute([1]))
