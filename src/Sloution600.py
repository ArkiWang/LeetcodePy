import numpy as np
class Solution:

    def findIntegers(self, num: int) -> int:
        bit = len(bin(num)) - 2
        print(bit)
        dp = np.zeros((bit, 2), int)
        dp[0] = [1, 1]
        sumd = 2
        for i in range(1, bit):
            if i == 1:
                dp[i][0] = dp[i-1][1]
            elif i == bit:

            else:
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
            sumd += sum(dp[i])
        print(dp)
        return sumd

sol = Solution()
res = sol.findIntegers(5)
print(res)



