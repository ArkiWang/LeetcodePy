from cmath import inf


class Solution:
    def cost(self, s: str, low: int, high: int):
        ss = list(s[low: high])
        re_ss = ss[::-1]
        cos = 0
        for i in range(len(ss)):
            if ss[i] != re_ss[i]:
                cos += 1
        return int(cos/2)

    def palindromePartition(self, s: str, k: int) -> int:
        dp = [[0] * (k+1) for _ in range(len(s) + 1)]
        #dp[i][j] i: 0.. len(s) j: 0..k


        for i in range(1, len(s) + 1):
            for j in range(1, k + 1):
                if i <= j:
                    continue
                if j < 2:
                    dp[i][j] = self.cost(s, 0, i)
                    continue
                minima = inf
                for i0 in range(j-1, i):
                    if minima == inf:
                        minima = dp[i0][j-1] + self.cost(s, i0, i)
                    else:
                        minima = min(minima, dp[i0][j-1] + self.cost(s, i0, i))
                dp[i][j] = minima

        print(dp)
        return dp[len(s)][k]


sol = Solution()
s = "abc"
k = 2
s = "aabbc"
k = 3
res = sol.palindromePartition(s, k)
print(res)

