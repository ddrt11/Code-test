class Solution:
    def intToRoman(self, num: int) -> str:
        # 把所有可能的数值和对应符号从大到小排列
        value_symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = []
        for val, sym in value_symbols:
            while num >= val:
                res.append(sym)
                num -= val
            if num == 0:
                break
        return ''.join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))
    print(s.intToRoman(58))
