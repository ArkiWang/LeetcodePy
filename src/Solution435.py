class Solution:
    def eraseOverlapIntervals2(self, intervals: [[int]]) -> int:
        n = len(intervals)
        if n < 1:return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j]+1 if intervals[j][1] <= intervals[i][0] else 0)
        return n - max(dp)

    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        n = len(intervals)
        if n < 1: return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        dp = [1] * n
        for i in range(1, n):
            dp[i] = max((dp[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1
        return n - max(dp)

intervals = [[1,100],[11,22],[1,11],[2,12]]
sol = Solution()
res = sol.eraseOverlapIntervals(intervals)
print(res)