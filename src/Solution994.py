import numpy as np
import copy
class Solution:
    def checkall(self, grid: [[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return False
        return True

    def rot_helper(self, rx, ry, grid:[[int]]) -> bool:
        flag = False
        if rx - 1 >= 0 and grid[rx - 1][ry] == 1:
            grid[rx - 1][ry] = 2
            flag = True
        if rx + 1 < len(grid) and grid[rx + 1][ry] == 1:
            grid[rx + 1][ry] = 2
            flag = True
        if ry - 1 >= 0 and grid[rx][ry - 1] == 1:
            grid[rx][ry - 1] = 2
            flag = True
        if ry + 1 < len(grid[rx]) and grid[rx][ry + 1] == 1:
            grid[rx][ry + 1] = 2
            flag = True
        return flag

    def orangesRotting(self, grid: [[int]]) -> int:
        lastcnt = -1
        cnt = 0
        while lastcnt != cnt:
            lastcnt = cnt
            lastgrid = copy.deepcopy(grid)
            flag = False
            Flag = False
            for i in range(len(lastgrid)):
                for j in range(len(lastgrid[i])):
                    if lastgrid[i][j] == 2:
                        flag = self.rot_helper(i, j, grid)
                        if flag: Flag = True
            if Flag: cnt += 1
            if self.checkall(grid):
                return cnt
        return -1




sol = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
grid = [[1]]
grid = [[1,2,1,1,2,1,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))