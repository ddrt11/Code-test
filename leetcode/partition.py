class Solution:
    def partition(self, s):
        res = []
        # 判断是否回文
        def is_pal(sub):
            return sub == sub[::-1]
        def backtrack(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            for i in range(start, len(s)):
                sub = s[start:i+1]
                if is_pal(sub):
                    path.append(sub)
                    backtrack(i+1, path)
                    path.pop()
        backtrack(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
