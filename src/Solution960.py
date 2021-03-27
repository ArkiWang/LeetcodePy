class Solution:
    def minDeletionSize(self, A: [str]) -> int:
        w = len(A[0])
        # dp[i] from i on
        dp = [1]*w

        for i in range(w-2, -1, -1):
            for j in range(i+1, w):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], dp[j]+1)
        return w - max(dp)

