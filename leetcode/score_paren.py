class Solution:
    def scoreOfParentheses(self, s):
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += 1 if v == 0 else 2*v
        return st[0]

if __name__ == "__main__":
    s = Solution()
    print(s.scoreOfParentheses("()"))
    print(s.scoreOfParentheses("(())"))
    print(s.scoreOfParentheses("()()"))
    print(s.scoreOfParentheses("((()))"))
