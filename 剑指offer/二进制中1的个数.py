# 方法一，按位与1，时间复杂度O(log2(n)), 空间复杂度O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

# 方法二，巧用n&(n-1), 时间复杂度O(M), M为2进制中1的个数, 空间复杂度O(1)
# n: 10101000
# (n-1): 二进制数字n最右边的1变成0,此1右边的0都变成1。10100111
# n&(n-1): 二进制数字n最右边的1变成0,其余不变。10100000
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n&(n-1)
        return res