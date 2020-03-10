# 时间复杂度O(MN),空间复杂度O(1),在原数组上进行修改
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        obstacleGrid = [[1 - obstacleGrid[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m): 
            if obstacleGrid[i-1][0] == 0: obstacleGrid[i][0] = obstacleGrid[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j-1] == 0: obstacleGrid[0][j] = obstacleGrid[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0: continue
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]



if __name__ == '__main__':
    obstacleGrid = [[0,1,0,0,0], [1,0,0,1,0], [0,0,0,0,0], [0,0,0,0,0]]
    # [[0,0],[1,0]]
    # [[0,0,0], [0,1,0], [0,0,0]]
    # [[0,1,0,0,0], [1,0,0,1,0], [0,0,0,0,0], [0,0,0,0,0]]
    model = Solution()
    res = model.uniquePathsWithObstacles(obstacleGrid)
    print(res)