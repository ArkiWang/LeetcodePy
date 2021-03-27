import numpy as np
class Solution:
    def maxSizeSlices(self, slices: [int]) -> int:
        n = len(slices)
        choose = int(n/3)
        dp = np.zeros((n+1, choose+1), int)
        dp[1][1] = slices[0]
        for i in range(3, n+1):
            for j in range(1, choose):
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+slices[i])


slices = [1,2,3,4,5,6]
