# 方法一, appendTail时间复杂度O(1), deleteHead时间复杂度为O(N), 空间复杂度O(N)
# 思路，用AB两个栈实现队列，appendTail操作队列和栈无区别，直接用栈的方式append就可以
# deleteHead操作栈和队列不同，做法是先将栈A的元素的pop出到B栈中，那么B栈就是A栈的反序
# 再pop出B栈的第一个元素就是deleteHead得到的元素，最后再将B栈的元素再反向输入到A栈中
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        if value: self.A.append(value)

    def deleteHead(self) -> int:
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        val = self.B.pop()
        while self.B:
            self.A.append(self.B.pop())
        return val


# 方法二：与方法一差不多，但是简单了些，不再将B的元素反向输入到A
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        if value: self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
        

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()