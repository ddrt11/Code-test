class Solution:
    def combine(self, n: int, k: int):
        res = []
        # start：从哪个数字开始选，path：当前选中的组合
        def backtrack(start, path):
            # 选够k个数字，加入结果
            if len(path) == k:
                res.append(path.copy())
                return
            # 从start开始，避免重复组合（如[1,2]和[2,1]只保留前者）
            for i in range(start, n+1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
