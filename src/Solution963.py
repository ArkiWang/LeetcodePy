class Solution:
    def isRect(self, points:[[]]) -> bool:
        x, y = 0, 0
        for i in range(4):
            x += points[i][0]
            y += points[i][1]
        x /= 4
        y /= 4
        for i in range(1, 4):
            if (points[i][0] - x)**2+(points[i][1] - y)**2 != (points[i-1][0] - x)**2 + (points[i-1][1] - y)**2:
                return False
        return True

    def minAreaFreeRect(self, points: [[int]]) -> float:
