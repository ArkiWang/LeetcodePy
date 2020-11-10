from typing import List
import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = np.zeros((m, n),int)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:dp[i][j]=1
                elif obstacleGrid[i][j] == 0:
                    if i>0 and j>0:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
                    elif i>0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
        return int(dp[m-1][n-1])

obstacle = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
solution = Solution()
res=solution.uniquePathsWithObstacles(obstacle)
print(res)
