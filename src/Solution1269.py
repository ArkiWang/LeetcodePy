import numpy as np
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps + 1)
        dp = np.zeros((steps, arrLen),int)#dp[i][j] how many ways ith step reaches j
        dp[0][0], dp[0][1] = 1, 1
        for i in range(1, steps):
            for j in range(arrLen):
                if j-1 >= 0 and j+1 < arrLen:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % (10**9 + 7)
                elif j-1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + dp[i - 1][j]) % (10**9 + 7)
                elif j+1 < arrLen:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] + dp[i - 1][j + 1]) % (10**9 + 7)
                else:
                    dp[i][j] = dp[i - 1][j] % (10**9 + 7)
        return dp[steps-1][0]


    ans = 0
    def numWays2(self, steps: int, arrLen: int) -> int:
        #remain0 left -1 right 1
        self.ans = 0
        self.helper(steps, arrLen,0,0)
        return self.ans

    def helper(self, steps: int, arrLen: int, currSum: int, currStep: int):
        if currStep < steps:
            for i in [-1, 0, 1]:
                if currSum+i < arrLen and currSum+i >= 0:
                    self.helper(steps, arrLen, currSum+i, currStep+1)
        elif currSum == 0:
            self.ans += 1

solution = Solution()
res = solution.numWays(430, 148488)
print(res)

#res = solution.numWays2(27,7)
#print(res)



