class Solution:
    def plusOne(self, digits):
        # 从最后一位开始遍历，模拟进位
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            # 如果当前位不等于10，说明没有进位，直接返回
            if digits[i] != 10:
                return digits
            # 等于10，置0，继续向前进位
            digits[i] = 0
        # 循环走完说明全部都是9，例如[9,9,9]，需要在最前面补1
        return [1] + digits

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([4,3,2,1]))
    print(s.plusOne([9]))
