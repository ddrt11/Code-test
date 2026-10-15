class Solution:
    def countAndSay(self, n):
        # 基础情况，n=1对应的字符串为"1"
        res = "1"
        # 从2循环到n，依次生成每一层的外观数列
        for i in range(2, n + 1):
            temp = ""
            j = 0
            # 遍历当前字符串，统计连续相同字符
            while j < len(res):
                cnt = 1
                # 若下一个字符和当前字符相同，计数增加，指针后移
                while j + 1 < len(res) and res[j] == res[j+1]:
                    cnt += 1
                    j += 1
                # 拼接「计数 + 字符」
                temp += str(cnt) + res[j]
                j += 1
            res = temp
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))
    print(s.countAndSay(1))
