class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s) - k + 1
        dp = [0]*n
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vowels:
                dp[0] += 1

        for i in range(1, n):
            dp[i] = dp[i-1] - (1 if s[i-1] in vowels else 0) + (1 if s[i+k-1] in vowels else 0)

        return max(dp)

s = "abciiidef"
k = 3
s = "leetcode"; k = 3
s = "novowels"
k = 1
sol = Solution()
res = sol.maxVowels(s, k)
print(res)