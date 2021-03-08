from copy import deepcopy

class Solution:
    klist = []
    def helper(self, i, k:[]) -> int:
        if len(k) < 1:return 1
        tmp = deepcopy(k)
        add = k[-1]
        ans = 1
        while i < len(tmp):
            if i == 0 or tmp[i] + add <= tmp[i-1]:
                k = deepcopy(tmp)
                k[i] += add
                k = k[:-1]
                if not self.klist.__contains__(k):
                    self.klist.append(k)
                    res = 1
                    for ki in k:
                        res *= ki
                    #print(res, k)
                    ans = max(res, ans)
            i += 1
        return ans


    def cuttingRope2(self, n: int) -> int:
        k = [1]*n
        self.klist = [k]
        ans, i = 1, 0
        while i < len(self.klist):
            k = self.klist[i]
            i += 1
            if len(k) > 2:
                ans = max(ans, self.helper(0, k))
            else:
                ans = max(ans, k[0]*k[1])

        return ans

    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max((i-j)*j,dp[j]*(i-j)))
        return dp[-1]
sol = Solution()
res = sol.cuttingRope(2)
print(res)


