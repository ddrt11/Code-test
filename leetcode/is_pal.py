class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
