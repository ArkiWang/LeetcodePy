class Solution:
    res = False
    def dfs(self, x: int, target: int, dic: {}):
        if x == target or (x in dic and target in dic[x]):
            self.res = True
        elif x in dic:
            for y in dic[x]:
                self.dfs(y, target, dic)

    def findWhetherExistsPath(self, n: int, graph: [[int]], start: int, target: int) -> bool:
        dic = {}
        for pair in graph:
            x, y = pair
            if x not in dic:
                dic[x] = {y}
            else:
                dic[x].add(y)
        print(dic)
        self.res = False
        self.dfs(start, target, dic)
        return self.res

n = 12
graph = [[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]]
start = 2
target = 3
n = 25
graph = [[0, 1], [0, 3], [0, 10], [0, 18], [1, 2], [1, 7], [1, 11], [1, 12], [2, 4], [2, 5], [2, 13], [2, 16], [3, 6], [3, 8], [4, 9], [5, 17], [7, 20], [7, 22], [8, 10], [10, 19], [11, 15], [13, 14], [14, 21], [15, 23], [19, 24], [20, 22]]
start = 0
target = 12
sol = Solution()
res = sol.findWhetherExistsPath(n, graph, start, target)
print(res)