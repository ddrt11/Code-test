class Solution:
    def combinationSum(self, candidates, target):
        res = []
        # 回溯函数，start控制起始位置，避免重复组合，cur是当前路径，total是当前总和
        def backtrack(start, cur, total):
            # 当前总和等于目标，把当前组合加入结果
            if total == target:
                res.append(cur.copy())
                return
            # 总和超过目标，直接返回，剪枝
            if total > target:
                return
            # 从start开始遍历，元素可以重复选取，所以下一轮i不变
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, cur, total + candidates[i])
                cur.pop()
        backtrack(0, [], 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7],7))
    print(s.combinationSum([2,3,5],8))
    print(s.combinationSum([2],1))
