
class Solution:
    def subsets(self, nums):
        res = []

        # 回溯：start控制起始下标，path保存当前子集
        def backtrack(start, path):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))
