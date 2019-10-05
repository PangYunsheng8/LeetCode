# 方法一：滑动窗口
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         length = len(s)
#         all_length = [0]
#         over_index = 0
#         for i in range(length):
#             while(over_index < length and s[over_index] not in s[i:over_index]):
#                 over_index += 1
#             all_length.append(over_index - i)
#         return max(all_length)


# 方法二：也算是滑动窗口，另一种写法，但是有点绕
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        fst, sec = 0, 1
        maxSub = sec - fst
        while sec < len(s):
            if s[sec] in s[fst:sec]:
                if maxSub < (sec-fst): maxSub = (sec-fst) 
                while s[fst] != s[sec]:
                    fst += 1
                fst += 1
            else:
                if maxSub < (sec-fst+1): maxSub = (sec-fst+1) 
            sec += 1
        return maxSub