# 思路，快速幂法
# x^n = x^(2/n) X x^(2/n) = (x^2)^(2/n), 可以通过这样的方法，每次将x->x^2, n->2/n,直到n降为0
# 特殊问题：在n->2/n时，涉及到n//2，有两种情况：
# 1)n为奇数时，x^n = x(x^2)^(n//2)
# 2)n为偶数时，x^n = (x^2)^(n//2)

# 转化为位运算：
# n // 2 => n >>= 1
# n % 2 => n & 1

# 时间复杂度O(log2(n)), 空间复杂度O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1 == 1: res *= x  # n & 1相当于n % 2
            x = x * x
            n = n >> 1 # 相当于n = n // 2
        return res