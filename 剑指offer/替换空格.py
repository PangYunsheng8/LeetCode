# 解法一: 先记录空格的位置，再利用字符串拼接来完成，每次替换后，字符串长度都增加了2
# 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def replaceSpace(self, s: str) -> str:
        pos = []
        for i in range(len(s)):
            if s[i] == " ": pos.append(i)
        
        for j in range(len(pos)):
            s = s[:j*2+pos[j]] + "%20" + s[j*2+pos[j]+1:]
        return s


# 解法二: 思路不变，但是不记录位置了，并且用list拼接代替字符串拼接，效率更高
class Solution:
    def replaceSpace(self, s: str) -> str:
        mystr = []
        for i in range(len(s)):
            if s[i] == " ": mystr.append("%20")
            else: mystr.append(s[i])
        return ''.join(mystr)