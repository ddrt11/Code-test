class Solution:
    def isValid(self, s):
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dic:
                if not stack:
                    return False
                top = stack.pop()
                if dic[c] != top:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))
