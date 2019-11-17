class Solution:
    def shiftGrid(self, grid, k: int):
        stack = []
        n = len(grid)
        m = len(grid[0])
        for _ in range(k):
            for i in range(n):
                stack.append(grid[i][-1])
                grid[i][1:] = grid[i][:m-1]
                if len(stack) > 1:
                    grid[i][0] = stack[0]
                    stack.pop(0)
            grid[0][0] = stack[0]
            stack.pop()
        return grid