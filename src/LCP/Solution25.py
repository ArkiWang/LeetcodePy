import numpy as np
from ctypes import c_longlong as ll
class Solution:
    def A(self, m, n):
        res = 1
        for i in range(n-m+1, n+1):
            res *= i
        return res

    def C(self, m, n):
        top = self.A(m, n)
        bot = self.A(m, m)
        res = int(top/bot)
        return res

    def c(self, m, n):
        k, ans = 1, 1
        while k <= n:
            ans = ((m-k+1) * ans) / k
            k += 1
        return ans


    def keyboard(self, k: int, n: int) -> int:
        dp = np.zeros((n+1, 27), ll)
        for i in range(27):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(1, 27):
                for x in range(k+1):
                    if i - x >=0:
                        dp[i][j] += dp[i-x][j-1]*self.c(i, x)
                dp[i][j] %= 1000000007

        return int(dp[n][26] % 1000000007)

sol = Solution()
res = sol.keyboard(5, 109)
print(res)