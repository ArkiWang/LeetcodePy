import numpy as np
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lens, lent = len(s), len(t)
        dp = np.zeros((lens, lent), int)

        for i in range(lens):
            if i == 0 and s[i] == t[0]:
                dp[i][0] = 1
            elif s[i] == t[0]:
                dp[i][0] = dp[i-1][0] + 1
            elif i > 0:
                dp[i][0] = dp[i-1][0]

        for j in range(1, lent):
            for i in range(j, lens):
                if s[i] == t[j]:
                    # 即可把当前纳入考虑 也可不把当前纳入考虑
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    #不把当前纳入考虑
                    dp[i][j] = dp[i - 1][j]

        print(dp)
        return dp[-1][-1]

s = "rabbbit"
t = "rabbit"
s = "babgbag"
t = "bag"
sol = Solution()
res = sol.numDistinct(s, t)
print(res)