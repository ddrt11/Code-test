class Solution:
    def restoreIpAddresses(self, s):
        res = []
        
        # 回溯：start当前截取位置，path存已选的IP段
        def backtrack(start, path):
            # 凑够4段且刚好用完所有字符，得到一个合法IP
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            
            # 每段最多取3位
            for i in range(start, min(start + 3, len(s))):
                sub = s[start:i+1]
                # 非法情况：数值超过255，或长度>1且以0开头（前导零）
                if int(sub) > 255 or (len(sub) > 1 and sub[0] == '0'):
                    continue
                path.append(sub)
                backtrack(i + 1, path)
                path.pop()  # 回溯
        
        backtrack(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("0000"))
