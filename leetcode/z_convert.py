class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur = 0
        down = False
        for c in s:
            rows[cur] += c
            if cur == 0 or cur == numRows -1:
                down = not down
            cur += 1 if down else -1
        return ''.join(rows)

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING",3))
    print(s.convert("PAYPALISHIRING",4))
    print(s.convert("A",1))
