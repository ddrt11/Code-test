class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            row = [1]*(i+1)
            # 首尾已经是1，只算中间
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
    print(s.generate(1))
