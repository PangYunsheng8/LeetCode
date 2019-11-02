class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        
        s = s.rstrip()
        index = 0
        for i in s[::-1]:
            if i == ' ': return index
            index+= 1
        return index