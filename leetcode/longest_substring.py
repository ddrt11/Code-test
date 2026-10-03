class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
