class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        # 先排序，方便跳过重复数字
        candidates.sort()
        def backtrack(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # 跳过同一层的重复元素，防止出现重复组合
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                # 每个元素只能用一次，下一轮start是i+1
                backtrack(i+1, cur, total + candidates[i])
                cur.pop()
        backtrack(0, [], 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5],8))
    print(s.combinationSum2([2,5,2,1,2],5))
