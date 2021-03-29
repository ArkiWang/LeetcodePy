import numpy as np
class Solution:
    def stoneGameV(self, stoneValue: [int]) -> int:
        n = len(stoneValue)
        sums = np.zeros((n, n), int)
        for i in range(n):
            for j in range(i, n):
                sums[i][j] = sum(stoneValue[i:j+1])

        def dfs(l, r):
            ans = 0
            for k in range(l, r):
                if sums[l][k] < sums[k+1][r]:
                    ans = max(ans, sums[l][k] + dfs(l, k))
                elif sums[l][k] == sums[k+1][r]:
                    ans = max(ans, sums[l][k] + max(dfs(l, k), dfs(k+1, r)))
                else:
                    ans = max(ans, sums[k+1][r] + dfs(k+1, r))
            return ans

        return dfs(0, n-1)

stoneValue = [6,2,3,4,5,5]
sol = Solution()
res = sol.stoneGameV(stoneValue)
print(res)
