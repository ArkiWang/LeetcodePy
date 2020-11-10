import numpy as np
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        if len(heights) == 0:return 0
        max_stack = []
        maxs = heights[0]
        for i in range(len(heights)):
            if len(max_stack) == 0 or max_stack[-1][0] <= heights[i]:
                max_stack.append([heights[i], i])
            else:
                top = max_stack[-1][1]
                while len(max_stack) > 0 and max_stack[-1][0] > heights[i]:
                    last = max_stack.pop()
                    if len(max_stack) > 0:
                        maxs = max(maxs, last[0] * (top - max_stack[-1][1]))
                    else:
                        maxs = max(maxs, last[0] * (top + 1))
                max_stack.append([heights[i], i])

        top = max_stack[-1][1]
        while len(max_stack) > 0:
            last = max_stack.pop()
            if len(max_stack) > 0:
                maxs = max(maxs, last[0] * (top - max_stack[-1][1]))
            else:
                maxs = max(maxs, last[0] * (top + 1))

        return maxs


    def largestRectangleArea2(self, heights: [int]) -> int:
        hlen = len(heights)
        #dp[i][j] the min number in range [i, j]
        dp = np.zeros((hlen, hlen), int)
        for i in range(hlen):
            for j in range(i, hlen):
                if i == j:
                    dp[i][j] = heights[j]
                else:
                    dp[i][j] = min(dp[i][j-1], heights[j])

        maxS = 0
        for i in range(hlen):
            for j in range(i, hlen):
                maxS = max(maxS, dp[i][j]*(j-i+1))

        return int(maxS)

sol = Solution()

heights = [0, 9]

heights = [5,4,1,2]
heights = [2,1,5,6,2,3]

heights = [1, 1]
heights = [2, 1, 2]
heights = [4,2,0,3,2,5]
heights = [12,11,10,9,8,7,6,5,4,3,2,1]
res = sol.largestRectangleArea(heights)
print(res)
res = sol.largestRectangleArea2(heights)
print(res)

d :dict