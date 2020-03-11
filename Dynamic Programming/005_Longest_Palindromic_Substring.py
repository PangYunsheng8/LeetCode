# 状态: p[i][j]: s中从第i个字符开始，到第j个字符是不是回文子串(bool)
# p[i][j] = True, when Si - Sj 是回文子串
#         = False, otherwise
# 状态转移方程: p[i][j] = (p[i+1][j-1]) and (Si == Sj)
# 初始值和临界条件: 对于长度为1和2的子串要单独进行判断，因为这两种子串不满足上述状态转移方程
# 计算顺序: 由小到大
# 思路: 
# 1)两个for循环，第一个for循环遍历子串长度，从1开始。第二个for循环遍历起始位置，从0开始
#   当外层for循环执行两轮后，可以得到长度为1和2的所有子串是否为回文串
# 2)继续遍历，从第三个for循环开始，可以应用上述状态转移方程求解更长子串是否为回文串。直至遍历结束。


# 时间复杂度O(N^2), 空间复杂度O(N^2)
class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        p = [[0 for _ in range(length)] for _ in range(length)]
        max_sub_str = ""

        for _len in range(1, length + 1):
            for start in range(length):
                end = start + _len - 1
                if end >= length: break
                
                p[start][end] = (_len == 1 or _len == 2 or p[start + 1][end - 1]) and s[start] == s[end]

                if p[start][end] and (end - start + 1) > len(max_sub_str): max_sub_str = s[start: end + 1]
        return max_sub_str


# 时间复杂度O(N^2), 空间复杂度O(N)
class Solution2:
    def longestPalindrome(self, s):
        length = len(s)
        p = [0 for _ in range(length)]
        max_sub_str = ""

        for i in range(length - 1, -2, -1):
            for j in range(length - 1, i - 1, -1):
                p[j] = s[i] == s[j] and (j - i < 3 or p[j-1])
                if p[j] and (j - i + 1) > len(max_sub_str): max_sub_str = s[i: j + 1]
        return max_sub_str                


if __name__ == "__main__":
    # model = Solution()
    model = Solution2()
    s = "babad"
    res = model.longestPalindrome(s)
    print(res)