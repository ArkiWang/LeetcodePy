import collections

import numpy as np
class Solution:
    Ans = 0
    def helper(self, i, hats:[[]], ans: set):
        if i < len(hats):
            for h in hats[i]:
                if h not in ans:
                    ans.add(h)
                    self.helper(i+1, hats, ans)
                    ans.remove(h)
        elif len(ans) == len(hats):
            self.Ans += 1

    def numberWays3(self, hats: [[int]]) -> int:
        ans = set()
        self.Ans = 0
        self.helper(0, hats, ans)
        return self.Ans

    def numberWays2(self, hats: [[int]]) -> int:
        mod = 10 ** 9 + 7
        # n个人
        n = len(hats)
        # 找到帽子编号的最大值，这样我们只需要求出 $f[maxhatid][2^n - 1]$ 作为答案
        maxHatId = max(max(ids) for ids in hats)

        # 对于每一顶帽子 h，hatToPerson[h] 中存储了喜欢这顶帽子的所有人，方便进行动态规划
        hatToPerson = collections.defaultdict(list)
        for i in range(n):
            for h in hats[i]:
                hatToPerson[h].append(i)

        f = [[0] * (1 << n) for _ in range(maxHatId + 1)]
        print(maxHatId, n, f)
        # 边界条件
        f[0][0] = 1
        for i in range(1, maxHatId + 1):
            for mask in range(1 << n):
                print(bin(mask))
                f[i][mask] = f[i - 1][mask]
                for j in hatToPerson[i]:
                    if mask & (1 << j):
                        f[i][mask] += f[i - 1][mask ^ (1 << j)]
                f[i][mask] %= mod
        print(f)
        return f[maxHatId][(1 << n) - 1]

    def numberWays(self, hats: [[int]]) -> int:
        mod = 10**9+7
        #人数
        n = len(hats)
        maxHat = 0
        for i in range(n):
            maxHat = max(maxHat, max(hats[i]))
        dp = [[0] * (1<<n) for _ in range(maxHat + 1)]
        hatToPerson = {}
        for i in range(n):
            for h in hats[i]:
                if h not in hatToPerson:
                    hatToPerson[h] = [i]
                else:
                    hatToPerson[h].append(i)
        dp[0][0] = 1
        for i in range(1, maxHat+1):
            for mask in range(1<<n):
                dp[i][mask] = dp[i-1][mask]
                if i in hatToPerson:
                    for j in hatToPerson[i]:
                        if mask & (1 << j):
                            dp[i][mask] += dp[i-1][(1<<j)^mask]
                dp[i][mask] %= mod
        print(dp)
        return dp[-1][-1]

hats = [[3,4],[4,5],[5]]
hats = [[3,5,1],[3,5]]
sol = Solution()
res = sol.numberWays(hats)
print(res)