def isHappy(n: int) -> bool:
    def ishappy(n):
        print(n)
        if n == 1:
            return True
        elif n < 10 and n !=1 :
            return False
        number = [int(i) for i in str(n)]
        n = 0
        for i in number:
            n += i*i
        ishappy(n)
    ishap = ishappy(n)

n = 19
ishap = isHappy(19)
print(ishap)
