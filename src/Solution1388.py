import numpy as np
class Solution:
    def maxSizeSlices(self, slices: [int]) -> int:
        def helper(slices: []):
            n = len(slices)
            choice = (n+1)//3
            # dp[i][j] 前i个里面选择j个的最大和
            dp = np.zeros((n + 1, choice + 1), int)
            for i in range(1, n + 1):
                for j in range(1, choice+1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1])
            print(dp)
            return dp[-1][-1]

        #成环首尾不能同时取得
        s1 = slices[1:]
        s2 = slices[:-1]
        return max(helper(s1), helper(s2))



slices = [1,2,3,4,5,6]
slices = [8,9,8,6,1,1]
slices = [4,1,2,5,8,3,1,9,7]
sol = Solution()
res = sol.maxSizeSlices(slices)
print(res)
