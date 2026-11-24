class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex+1):
            # 倒着更新，避免覆盖前面的值
            for j in range(i-1, 0, -1):
                row[j] = row[j-1] + row[j]
            row.append(1)
        return row

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
    print(s.getRow(0))
    print(s.getRow(1))
