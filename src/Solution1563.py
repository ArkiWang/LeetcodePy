import numpy as np
class Solution:
    def stoneGameV(self, stoneValue: [int]) -> int:
        stoneValue = sorted(stoneValue)
        print(stoneValue)
        #dp[i][j] stoneValue[i:j+1] Alice所得的最大值
        n = len(stoneValue)
        dp = np.zeros((n, n), int)
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if j == i + 1:
                    dp[i][j] += min(stoneValue[i:j+1])
                else:
                    for k in range(i+1, j):
                        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])


        print(dp)
        return dp[0][-1]

stoneValue = [6,2,3,4,5,5]
sol = Solution()
res = sol.stoneGameV(stoneValue)
print(res)
