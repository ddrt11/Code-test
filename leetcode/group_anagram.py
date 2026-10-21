from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for s in strs:
            # 将字符串排序后的结果作为哈希表的key
            key = "".join(sorted(s))
            dic[key].append(s)
        # 将字典的值转为列表返回
        return list(dic.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
