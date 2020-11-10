import numpy as np
class Solution:
    #A = Y2 - Y1 B = X1 - X2 C = X2Y1 - X1Y2
    # Ax + By + C = 0
    def atLine(self, a: [], b: [], x: []):
        B = a[0] - b[0]
        A = b[1] - a[1]
        C = b[0]*a[1] - a[0]*b[1]
        """
        mc = self.largestcommon(A, B)
        if mc != 0:
            A = int(A/mc)
            B = int(B/mc)
        """
        if A*x[0] + B*x[1] + C == 0:
            return True
        return False

    def largestcommon(self, a: int, b: int) -> int:
        if a < b:
            smaller = a
        smaller = b
        maxc = 0
        for i in range(1, smaller):
            if a%i == 0 and b%i == 0:
                maxc = i
        return maxc



    def bestLine(self, points: [[int]]) -> [int]:
        max = 2
        s = [0, 1]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cnt = 2
                for k in range(j+1, len(points)):
                    if self.atLine(points[i], points[j], points[k]):
                        cnt += 1
                if max < cnt:
                    s = [i, j]
                    max = cnt
                    print("s: {}, max: {}".format(s, max))
        return s

points = [[23064,-1044],[0,22969],[17805,40898],[29725,-1778],[-32070,-2148],[-19027,-2055],[-679,-41065],[12043,-16880],[21838,13404],[22690,-6475],[21585,-19101],[7577,-14359],[-20014,-40714],[20942,-19286],[12648,21299],[-36169,-11846],[3595,-19224],[27974,26651],[25899,12871],[-13881,-24276],[16833,-19449],[-13881,5948],[-48591,29692],[17406,-39601],[24765,7305],[-41894,-12128],[13645,-12514],[17119,-45877],[27715,-3120],[10537,-33802],[-36719,-39521],[3328,-16834],[25332,10088],[-23069,-31890],[4192,28773],[20987,-7179],[29525,-25688],[-5450,-25263],[-14571,-26940],[-31236,17820],[-2435,-23250],[28720,-2449],[5905,7021],[-48683,-2355],[-64140,-27265],[20829,-17796],[21104,13825],[-30954,-26421]]
points = [[-3320,51525],[-2214,-4833],[2400,13565]]
sol = Solution()
s = sol.bestLine(points)
print(s)