class Solution:
    flag = False
    # [low, high)
    lastdiv = -1
    ids = set()

    def leftbranch(self, low1, high1, low2, high2, div1, div2, s1, s2, id) -> bool:
        if s1 == s2:
            self.flag = True
        if div1 != high1 and s1[low1: div1] != s2[low2: div2]:
            self.helper(low1, div1, low2, div2, s1, s2, len(self.ids))
            
        if div1 != high1 and s1[div1: high1] != s2[div2: high2]:
            self.helper(div1, high1, div2, high2, s1, s2)
        if s1[low1: high1] == s2[low2: high2]:return True
        return False

    def rightbranch(self, low1, high1, low2, high2, div1, div2, s1, s2, id) -> bool:
        s1 = s1[:low1] + s1[div1: high1] + s1[low1: div1] + s1[high1:]
        if s1 == s2:
            self.flag = True
        if div2 != high1 and s1[low1: div2] != s2[low2: div2]:
            self.helper(low1, div2, low2, div2, s1, s2)
        if div2 != high1 and s1[div2: high1] != s2[div2: high2]:
            self.helper(div2, high1, div2, high2, s1, s2)
        if s1[low1: high1] == s2[low2: high2]: return True
        return False

    def helper(self, low1: int, high1: int, low2: int, high2: int, s1, s2, id = -1) :
        div1 = -1
        if not self.flag and low1 <= high1 and s1 != s2:
            resl = self.getleftpart(s1[low1: high1], s2[low2: high2])
            resr = self.getrightpart(s1[low1: high1], s2[low2: high2])
            for (divl1, divl2) in resl:
                # choose which one to do the first
                # both from left
                divl1 += low1
                divl2 += low2
                if divl1 != low1 and divl1 < high1 and sorted(s1[divl1: high1]) == sorted(s2[divl2: high2]):
                    div1, div2 = divl1, divl2
                    ans = self.leftbranch(low1, high1, low2, high2, div1, div2, s1, s2, id)
                    if ans:
                        s1 = s1[:low1] + s2[low2: high2] + s1[high1:]
                        break
            for (divr1, divr2) in resr:
                divr1 += low1
                divr2 += low2
                print("{}: {}".format(s1[low1: divr1], s2[divr2: high2]))
                # one from left while the other from right
                if divr1 != low1 and divr1 < high1 and not self.flag and sorted(s1[divr1: high1]) == sorted(
                        s2[low2: divr2]):
                    div1, div2 = divr1, divr2
                    ans = self.rightbranch(low1, high1, low2, high2, div1, div2, s1, s2, id)
                    if ans:
                        s1 = s1[:low1] + s2[low2: high2] + s1[high1:]
                        break


            if div1 == -1 or div1 == self.lastdiv: return
            self.lastdiv = div1

            print("s1: {} ; s2: {}".format(s1[low1: high1], s2[low2: high2]))
            if s1 == s2:
                self.flag = True

        elif s1 == s2:
            self.flag = True


    def getleftpart(self, s1: str, s2: str) -> []:
        i = 1
        j = 1
        res = []
        while i < len(s1) and j < len(s2):
            if sorted(s1[:i]).__eq__(sorted(s2[:j])):
                res.append((i,j))
            i += 1
            j += 1
        return res

    def getrightpart(self, s1: str, s2: str) -> []:
        i = 1
        j = len(s2) - 1
        res = []
        while i <= len(s1) and j >= 0:
            if sorted(s1[:i]).__eq__(sorted(s2[j:])):
                res.append((i, j))
            i += 1
            j -= 1
        return res

    def preprocess(self, s1: str, s2: str):
        if s1[0] == s2[-1] or s1[-1] == s2[0]:
            return s1, s2
        begin = 0
        while s1[begin] == s2[begin] and begin < len(s1):
            begin += 1
        end = len(s1) - 1
        while s1[end] == s2[end] and end >= 0:
            end -= 1
        news1 = s1[begin: end + 1]
        news2 = s2[begin: end + 1]
        print("preprocess s1: {}, s2: {}".format(news1, news2))
        return news1, news2

    def precheck(self, s1, s2) -> bool:
        ds1 = {}
        ds2 = {}
        for i in range(len(s1)):
            if s1[i] not in ds1:
                ds1[s1[i]] = 1
            else:
                cnt = ds1.get(s1[i])
                ds1[s1[i]] = cnt + 1
            if s2[i] not in ds2:
                ds2[s2[i]] = 1
            else:
                cnt = ds2.get(s2[i])
                ds2[s2[i]] = cnt + 1
        ds1 = dict(sorted(ds1.items(), key=lambda kv: kv[0]))
        ds2 = dict(sorted(ds2.items(), key=lambda kv: kv[0]))
        if ds1 == ds2: return True
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        self.flag = False
        self.lastdiv = -1
        s1, s2 = self.preprocess(s1, s2)
        if self.precheck(s1, s2):
            self.helper(0, len(s1), 0, len(s2), s1, s2)
        if self.flag:
            s1, s2 = self.preprocess(s2, s1)
            if self.precheck(s1, s2):
                self.helper(0, len(s1), 0, len(s2), s1, s2)
        return self.flag

s1 = "a"
s2 = "b"
s1 = "abc"
s2 = "acb"
s1 = "abc"
s2 = "cba"
s1 = "great"
s2 = "rgeat"
s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"
s1 = "aa"
s2 = "ab"
s1 = "abcdd"
s2 = "dbdac"
s1 = "aaccd"
s2 = "acaad"
s1 = "hobobyrqd"
s2 = "hbyorqdbo"

s1 = "cbcccccbbabcbac"
s2 = "bbccaccbcbcabcc"
s1 = "oatzzffqpnwcxhejzjsnpmkmzngneo"
s2 = "acegneonzmkmpnsjzjhxwnpqffzzto"
s1 = "abcd"
s2 = "dacb"
s1 = "abbbcbaaccacaacc"
s2 = "acaaaccabcabcbcb"
s1 = "dbdac"
s2 = "abcdd"
s1 = "great"
s2 = "tager"
s1 = "abcd"
s2 = "badc"
sol = Solution()
res = sol.isScramble(s1, s2)
print(res)
