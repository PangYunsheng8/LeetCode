# DP, 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1

        f_list = [0, 1]
        for i in range(2, n + 1):
            x = f_list[i - 1] + f_list[i - 2]
            f_list.append(x)
        return f_list[-1] % 1000000007


# DP, 时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1

        pre, cur = 0, 1
        for i in range(2, n + 1):
            temp = cur
            cur = pre + cur
            pre = temp
        return cur % 1000000007


# DP, 时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007