class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(path, open, close):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open < n:
                path.append("(")
                backtrack(path, open+1, close)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(path, open, close+1)
                path.pop()
        backtrack([], 0, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))
