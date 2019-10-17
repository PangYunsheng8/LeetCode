# 方法一：把三个字母组成的单词按ASCII的顺序排序，作为键来构建一个哈希表
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for item in strs:
            value = "".join(list(sorted(item)))
            if value in res:
                res[value].append(item)
            else:
                res[value] = [item]
        result = []
        for _, v in res.items():
            result.append(v)
        return result
            