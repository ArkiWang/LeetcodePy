class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j])*max(dp[i-j], i-j))

        return dp[-1]

sol = Solution()
res = sol.integerBreak(10)
print(res)