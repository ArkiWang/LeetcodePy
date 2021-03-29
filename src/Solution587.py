from cmath import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    def Left_index(self, points):
        '''
        Finding the left most point
        '''
        minn = 0
        for i in range(1, len(points)):
            if points[i].x < points[minn].x:
                minn = i
            elif points[i].x == points[minn].x:
                if points[i].y > points[minn].y:
                    minn = i
        return minn

    def orientation(self, p, q, r):
        '''
        To find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are colinear
        1 --> Clockwise
        2 --> Counterclockwise
        '''
        val = (q.y - p.y) * (r.x - q.x) - \
              (q.x - p.x) * (r.y - q.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def convexHull(self, points, n):
        # There must be at least 3 points
        if n < 3:
            return

        # Find the leftmost point
        l = self.Left_index(points)

        hull = []

        p = l
        q = 0
        while (True):

            # Add current point to result
            hull.append(p)

            q = (p + 1) % n

            for i in range(n):

                # If i is more counterclockwise
                # than current q, then update q
                if (self.orientation(points[p],
                                points[i], points[q]) == 2):
                    q = i
            p = q

            # While we don't come to first point
            if (p == l):
                break

        ans = []
        # Print Result
        for each in hull:
            #print(points[each].x, points[each].y)
            ans.append([points[each].x, points[each].y])
        return ans

    def addPonints(self, ans: [], points: []):

        i = 0
        l = ans[0]
        add = []
        while i < len(ans):
            r = ans[i]
            i += 1
            for p in points:
                if p not in ans and self.orientation(Point(l[0], l[1]), Point(p[0], p[1]), Point(r[0], r[1])) == 0 and p[0] >= min(l[0], r[0]) and p[0] <= max(l[0], r[0]) and p[1] >= min(l[1], r[1]) and p[1] <= max(l[1], r[1]):
                    add.append(p)
            l = r
        r = ans[0]
        for p in points:
            if p not in ans and self.orientation(Point(l[0], l[1]), Point(p[0], p[1]), Point(r[0], r[1])) == 0 and p[
                0] >= min(l[0], r[0]) and p[0] <= max(l[0], r[0]) and p[1] >= min(l[1], r[1]) and p[1] <= max(l[1],
                                                                                                              r[1]):
                add.append(p)
        return add

    def outerTrees(self, points: [[int]]) -> [[int]]:
        Points = []
        for (x, y) in points:
            Points.append(Point(x,y))

        ans = self.convexHull(Points, len(Points))
        print(ans)
        if ans is None: return points
        add = self.addPonints(ans, points)
        return ans+add



points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
points = [[5,3],[7,5]]
points = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0]]
sol = Solution()
res = sol.outerTrees(points)
print(res)
