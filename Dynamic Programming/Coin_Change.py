# 有三个面值的硬币，分别是2元，5元和7元。现在希望用最少的硬币数量得到27元，求最少的硬币数量。
class Solution:
    def coin_change(self, target: int) -> int:
        f = [float('inf') for _ in range(target + 1)]

        f[0] = 0
        for i in range(2, target + 1):
            coin_2 = f[i - 2] + 1 if i - 2 >= 0 else float('inf')
            coin_5 = f[i - 5] + 1 if i - 5 >= 0 else float('inf')
            coin_7 = f[i - 7] + 1 if i - 7 >= 0 else float('inf')
            f[i] = min(coin_2, coin_5, coin_7)
        return f[-1]


if __name__ == '__main__':
    cc = Solution()
    res = cc.coin_change(27)
    print(res)