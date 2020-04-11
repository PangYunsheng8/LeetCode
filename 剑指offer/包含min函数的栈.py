class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.sort = []

    def push(self, x: int) -> None:
        self.elements.append(x)
        if not self.sort: self.sort.append(x)
        else:
            if self.sort[-1] >= x: self.sort.append(x)

    def pop(self) -> None:
        if self.elements.pop() == self.sort[-1]:
            self.sort.pop()

    def top(self) -> int:
        return self.elements[-1]

    def min(self) -> int:
        return self.sort[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()