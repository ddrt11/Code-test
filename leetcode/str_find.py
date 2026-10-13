class Solution:
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
    print(s.strStr("leetcode", "leeto"))
