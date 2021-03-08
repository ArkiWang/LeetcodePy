import numpy as np
class Solution:
    #the maximum number of inverse-pairs of length n is n*(n-1)/2
    def kInversePairs2(self, n: int, k: int) -> int:
        if k == 0:return 1
        max_in = int(n*(n-1)/2)
        if k > max_in: return 0
        dp = np.zeros((n+1, k+1), int)
        for i in range(1, n+1):
            dp[i][0] = 1
            dp[i][1] = i-1
            for j in range(2, k+1):
                for x in range(min(j+1,i)):
                    #向前i-1位查值 最多可创造i-1个逆序对
                    dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % (10**9 + 7)
        print(dp)
        return dp[-1][-1]

    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0: return 1
        max_in = int(n * (n - 1) / 2)
        if k > max_in: return 0
        dp = np.zeros((n + 1, k + 1), int)
        for i in range(1, n + 1):
            dp[i][0] = 1
            dp[i][1] = i - 1
            for j in range(2, min(max_in, k) + 1):
                '''
                f(i, j) = f(i - 1, j) + f(i - 1, j - 1) + ... + f(i - 1, j - i + 1)
                f(i, j - 1) = f(i - 1, j - 1) + f(i - 1, j - 2) + ... + f(i - 1, j - i)
                f(i, j) - f(i - 1, j) = f(i, j - 1) - f(i - 1, j - i)
                f(i, j) = f(i, j - 1) + f(i - 1, j) - f(i - 1, j - i)
                '''
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] - (dp[i - 1][j - i] if j - i >= 0 else 0)) % (10 ** 9 + 7)
        print(dp)
        return dp[-1][-1]

sol = Solution()
res = sol.kInversePairs(3, 2)
print(res)