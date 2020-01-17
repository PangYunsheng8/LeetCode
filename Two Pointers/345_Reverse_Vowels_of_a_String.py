class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U",]
        n = len(s)
        left, right = 0, n - 1
        s_list = list(s)
        while left < right:
            while s_list[left] not in vowel and left < n - 1: left += 1
            while s_list[right] not in vowel and right > 0: right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s[left]
                left += 1
                right -= 1
        return ''.join(s_list)

model = Solution()
res = model.reverseVowels("a.b,.")
print(res)