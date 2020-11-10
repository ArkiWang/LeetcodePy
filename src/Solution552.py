class Solution:

    def generateFullPermutation(self, high: int, low:int):
        if high <= 0: return 0
        res = 1
        while high > low:
            res *= high
            high -= 1
        return res
    def generateCombinationNum(self, m: int, n: int) -> int:
        amn = self.generateFullPermutation(m, m-n)
        ann = self.generateFullPermutation(n, 0)
        res = int(amn/ann)
        return res

    def checkRecord2(self, n: int) -> int:
        cn2 = self.generateCombinationNum(n, 2)
        cn_21 = self.generateCombinationNum(n-2, 1)
        cn1 = self.generateCombinationNum(n, 1)
        cn_11 = self.generateCombinationNum(n-1, 1)
        #n- 3*int((n+1)/3) + 2*int((n+1)/3)
        maxL = n - int((n+1)/3)
        res = cn2*cn_21 + cn1* cn_11 + cn2 + cn1 + cn1 + 1
        res = int(res)
        return res

sol = Solution()
print(sol.checkRecord(2))
