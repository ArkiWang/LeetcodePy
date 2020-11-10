import numpy as np
class Solution:
    def max_profit_per_worker(self, worker:int, difficulty: [int], profit: [int]) -> int:
        maxp = 0
        for i in range(len(difficulty)):
            if worker >= difficulty[i]:
                maxp = max(maxp, profit[i])
        return maxp

    def maxProfitAssignment(self, difficulty: [int], profit: [int], worker: [int]) -> int:
        sortindexes = np.argsort(profit)
        profit = np.array(profit)[sortindexes]
        difficulty = np.array(difficulty)[sortindexes]
        sum = 0
        for i in range(len(worker)):
            # sum += self.max_profit_per_worker(worker[i], difficulty, profit)
            indexes = np.argwhere(np.array(difficulty) <= worker[i]).reshape(-1)
            if len(indexes) < 1: continue
            wprofit = np.array(profit)[indexes]
            #sum += np.max(wprofit)
            sum += wprofit[-1]
        return sum

sol = Solution()
difficulty=[85,47,57]
profit=[24,66,99]
worker=[40,25,25]

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

difficulty = [68,35,52,47,86]
profit = [67,17,1,81,3]
worker = [92,10,85,84,82]

res = sol.maxProfitAssignment(difficulty, profit, worker)
print(res)