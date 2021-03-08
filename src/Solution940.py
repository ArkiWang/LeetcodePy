class Solution:

    def distinctSubseqII(self, S: str) -> int:
        dp = [0] * (len(S)+1)
        dp[0] = 1
        last = {}
        for i in range(len(S)):
            dp[i+1] = 2*dp[i]
            if S[i] in last:
                dp[i+1] -= dp[last[S[i]]]
            last[S[i]] = i
        print(dp)
        return (dp[-1]-1) % (10**9+7)

    def distinctSubseqII2(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i
        print(dp)
        return (dp[-1] - 1) % (10 ** 9 + 7)


S = "abc"
S = "pcrdhwdxmqdznbenhwjsenjhvulyve"
S = "lee"
sol = Solution()
res = sol.distinctSubseqII(S)
print(res)
res = sol.distinctSubseqII2(S)
print(res)
