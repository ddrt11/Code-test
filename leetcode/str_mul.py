class Solution:
    def multiply(self, num1, num2):
        # 其中一个是0直接返回"0"
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        # 乘积最多m+n位，初始化数组存储每一位结果
        arr = [0] * (m + n)
        # 逆序遍历两个字符串
        for i in range(m-1, -1, -1):
            a = int(num1[i])
            for j in range(n-1, -1, -1):
                b = int(num2[j])
                # 相乘结果放到对应位置
                temp = a * b
                # 叠加到原来位置
                p1 = i + j
                p2 = i + j + 1
                sum_val = temp + arr[p2]
                arr[p2] = sum_val % 10
                arr[p1] += sum_val // 10
        # 转字符串，去掉前导0
        s = ""
        for num in arr:
            if not (s == "" and num == 0):
                s += str(num)
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.multiply("2","3"))
    print(s.multiply("123","456"))
