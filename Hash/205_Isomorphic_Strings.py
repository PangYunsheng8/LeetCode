class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp = {}
        values = set()
        for index, char in enumerate(s):
            # 如果之前没出现过该字符，判断该字符对应的映射是否已存在，若存在返回false，否则继续
            if char not in temp:
                if t[index] in values:
                    return False
                temp[char] = t[index]
                values.add(t[index])
            # 如果之前出现过该字符，判断该字符对应的映射是否与之前相等，若不等返回false，否则继续
            else:
                if t[index] != temp[char]:
                    return False
        return True