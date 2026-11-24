class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            # 左指针跳过非字母数字
            while l < r and not s[l].isalnum():
                l += 1
            # 右指针跳过非字母数字
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
