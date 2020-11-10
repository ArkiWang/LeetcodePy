import numpy as np
class Solution:
    def findTheCity(self, n: int, edges: [[int]], distanceThreshold: int) -> int:
        # dp[i][j] distance of city i to j
        dp = np.zeros((n, n), int)
        dp.fill(-1)
        for i in range(n):
            dp[i][i] = 0
        # initializer
        for edge in edges:
            dp[edge[0]][edge[1]] = edge[2]
            dp[edge[1]][edge[0]] = edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] > -1 and dp[j][k] > -1 and (dp[i][j] > dp[i][k] + dp[k][j] or dp[i][j] == -1):
                        dp[i][j] = dp[i][k] + dp[k][j]
        minc = n
        pset = set()
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dp[i][j] > 0 and dp[i][j] <= distanceThreshold:
                    cnt += 1
            if minc >= cnt:
                pset.clear()
                minc = cnt
                pset.add(i)

        return pset.pop()



n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

sol = Solution()
res = sol.findTheCity(n, edges, distanceThreshold)
print(res)