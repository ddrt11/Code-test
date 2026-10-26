class Solution:
    def lengthOfLastWord(self, s):
        cnt = 0
        i = len(s) - 1
        # 从后往前跳过末尾所有空格
        while i >= 0 and s[i] == ' ':
            i -= 1
        # 统计最后一个单词的字符数
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))
