class Solution:
    def kmp_next(self, p: str) -> []:
        next = [0]*len(p)
        i = -1
        j = 0
        while j < len(p):
            next[j] = i
            i += 1
            j += 1
            if p[i] == p[j]:
                next[j] = next[i] + 1
            else:
                j = next[j]
        return next



    def helper(self, str1: str, str2: str, i: int, j: int, res: str) -> str:
        if i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                return self.helper(str1, str2, i+1, j+1, res + str1[i])
            else:
                res1 = self.helper(str1, str2, i+1, j, res + str1[i])
                res2 = self.helper(str1, str2, i, j+1, res + str2[j])
                if len(res1) < len(res2):return res1
                return res2
        elif i < len(str1):
            return res + str1[i:]
        elif j < len(str2):
            return res + str2[j:]
        else:
            return res

    def shortestCommonSupersequence2(self, str1: str, str2: str) -> str:
        if str1 == None:
            return str2
        if str2 == None:
            return str1
        if str1.__contains__(str2):
            return str1
        if str2.__contains__(str1):
            return str2
        res = self.helper(str1, str2, 0, 0, "")
        print(res)
        maxc = 0
        boolj = False
        posi = -1; posj = -1
        for i in range(len(str1)):
            if len(str1) - i <= len(str2) and str2[:len(str2) - (len(str1) - i)] == str1[i:]:
                cnt = len(str1) - i
                if cnt > maxc:
                    maxc = cnt
                    posi = i
        for j in range(len(str2)):
            if len(str2) - j <= len(str1) and str1[:len(str1) - (len(str2) - j)] == str2[j:]:
                cnt = len(str2) - j
                if cnt > maxc:
                    maxc = cnt
                    posj = j
                    boolj = True
        if boolj:
            return str2[: posj] + str1
        else:
            return str1[: posi] + str2

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1) + 1
        n = len(str2) + 1
        dp = [[''] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                elif len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        lcs = dp[m-1][n-1]
        print("largest common sequence is: {}".format(lcs))
        i = 0; j = 0; res = ''
        for lc in lcs:
            while i < m and str1[i] != lc:
                res += str1[i]
                i += 1
            while j < n and str2[j] != lc:
                res += str2[j]
                j += 1
            res += lc
            if str1[i] == lc:
                i += 1
            if str2[j] == lc:
                j += 1
        res += str1[i:]
        res += str2[j:]
        return res


sol = Solution()
str1 = "abac"
str2 = "cab"
str1 = "bbbaaaba"
str2 = "bbababbb"

str1 = "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb"
str2 = "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa"

str1 = "abac"
str2 = "cab"

str1 = "babbbbaa"
str2 = "baabbbbba"
res = sol.shortestCommonSupersequence(str1, str2)
print(res)



