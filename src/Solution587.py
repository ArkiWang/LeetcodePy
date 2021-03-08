from cmath import sqrt


class Solution:
    def operation(self, p:[], q:[], r:[]) -> bool:
        res1 = (q[0] - p[0])*(r[1] - q[1]) - (q[1] - p[1])*(r[0] - q[0])
        res2 = (q[1] - p[1])*(r[0] - q[0]) - (r[1] - q[1])*(q[0] - p[0])
        if res1 > 0 and res2 < 0: return True
        return False

    def inBetween(self, p:[], q:[], points:[[]]) -> []:
        v = (p[1] - q[1])/(p[0] - q[0])
        d = sqrt((p - q)**2)
        ans = []
        for point in points:
            dp = sqrt((points - q)**2)
            vp = (p[1] - points[1])/(p[0] - point[0])
            if vp == v and dp <= d:
                ans.append(point)
        return ans

    def outerTrees(self, points: [[int]]) -> [[int]]:
        points = sorted(points, key=lambda x: x[0])
        for p in points:
            for q in points:
                if q != p and 
