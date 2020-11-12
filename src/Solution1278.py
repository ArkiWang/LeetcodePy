class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        #dp[i][j] = k modify k letters to make s[0, j] palindrome in j subs
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    dp[i][j] =