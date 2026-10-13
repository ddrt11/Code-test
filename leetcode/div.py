
class Solution:
    def divide(self, dividend, divisor):
        MAX = 2**31 - 1
        MIN = -2**31
        if dividend == MIN and divisor == -1:
            return MAX
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            temp = b
            cnt = 1
            while a >= temp << 1:
                temp <<= 1
                cnt <<= 1
            a -= temp
            res += cnt
        return sign * res

if __name__ == "__main__":
    s = Solution()
    print(s.divide(10, 3))
    print(s.divide(7, -3))
