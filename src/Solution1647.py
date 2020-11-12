class Solution:
    def minDeletions(self, s: str) -> int:
        sdic = {}
        for i in range(len(s)):
            if s[i] not in sdic:
                sdic[s[i]] = 1
            else:
                cnt = sdic.get(s[i])
                sdic[s[i]] = cnt+1
        sdv = list(sorted(sdic.items(), key=lambda kv: kv[1]))
        sdv = [e[1] for e in sdv]
        cnt = 0
        for i in range(len(sdv)-2, -1, -1):
            if sdv[i] >= sdv[i + 1]:
                if sdv[i + 1] > 0:
                    cnt += (sdv[i] - sdv[i + 1] + 1)
                    sdv[i] -= (sdv[i] - sdv[i+1] + 1)
                else:
                    cnt += sdv[i]
                    sdv[i] = 0
        return cnt

sol = Solution()
s = "aaabbbcc"
s = "ceabaacb"
#s = "aab"
#s = "abcabc"
#s = "bbcebab"
res = sol.minDeletions(s)
print(res)





