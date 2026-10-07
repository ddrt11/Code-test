class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # 取最短字符串作为比较上限
        shortest = min(strs, key=len)
        for idx, char in enumerate(shortest):
            for word in strs:
                if word[idx] != char:
                    return shortest[:idx]
        return shortest

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
