class Solution:
    flag = False
    # [low, high)
    lastdiv = -1
    s1: str
    s2: str
    def helper(self, low1: int, high1: int, low2: int, high2: int) -> int:
        div1 = -1
        if not self.flag and low1 < high1 and self.s1 != self.s2:
            print("s1: {} ; s2: {}".format(self.s1[low1: high1], self.s2[low2: high2]))
            divl1, divl2 = self.getleftpart(self.s1[low1: high1], self.s2[low2: high2])
            divl1 += low1; divl2 += low2
            divr1, divr2 = self.getrightpart(self.s1[low1: high1], self.s2[low2: high2])
            divr1 += low1; divr2 += low2
            # both from left
            #if (divl1 >= divr1 and divl1 != high1) or divr1 == high2:
            #if divl1 <= divr1:
            if divl1 != low1 and divl1 <= high1:
                div1, div2 = divl1, divl2
                if div1 != high1 and self.s1[low1: div1] != self.s2[low2: div2]:
                    self.helper(low1, div1, low2, div2)
                if div1 != high1 and self.s1[div1: high1] != self.s2[div2: high2]:
                    self.helper(div1, high1, div2, high2)
                if self.s1[div1: high1] + self.s1[low1: div1] == self.s2[low2: high2]:
                    self.s1 = self.s1[:low1] + self.s1[div1: high1] + self.s1[low1: div1] + self.s1[high1:]
                #print("left s1: {} ; s2: {}".format(self.s1[low1: high1], self.s2[low2: high2]))

            if self.s1 == self.s2:
                self.flag = True

            #else:# on from left the other from right
            if divr1 != low1 and divr1 <= high1 and not self.flag:
                div1, div2 = divr1, divr2
                if div1 != high1 and self.s1[low1: div1] != self.s2[div2: high2]:
                    self.helper(low1, div1, div2, high2)
                if div1 != high1 and self.s1[div1: high1] != self.s2[low2: div2]:
                    self.helper(div1, high1, low2, div2)
                if self.s1[div1: high1] + self.s1[low1: div1] == self.s2[low2: high2]:
                    self.s1 = self.s1[:low1] + self.s1[div1: high1] + self.s1[low1: div1] + self.s1[high1:]
                #print("right s1: {} ; s2: {}".format(self.s1[low1: high1], self.s2[low2: high2]))

            if self.s1 == self.s2:
                self.flag = True
            if div1 == -1 or div1 == self.lastdiv: return -1
            self.lastdiv = div1

           # print("s1: {} ; s2: {}".format(self.s1[low1: high1], self.s2[low2: high2]))


           # if self.s1[low1: high1] != self.s2[low2: high2]:
            #    self.s1 = self.s1[:low1] + self.s1[div1: high1] + self.s1[low1: div1] + self.s1[high1:]

        elif self.s1 == self.s2:
            self.flag = True
        return 0

    def getleftpart(self, s1: str, s2: str) ->():
        i = 0; j = 0
        li = []; lj = []
        pi, pj = 0,0
        lpi, lpj =0,0
        while i < len(s1) and j < len(s2) and ((pi == 0 and pj == 0) or s1[i] == s2[j]):
            lpi, lpj = pi, pj
            li.append(s1[i])
            lj.append(s2[j])
            i += 1
            j += 1
            #if li == lj: return i, j
            if sorted(li).__eq__(sorted(lj)):
                #pi, pj = i, j
                return i,j
        if pi == len(s1) and lpi != 0:
            return lpi,lpj
        return pi, pj

    def getrightpart(self, s1: str, s2: str) ->():
        i = 0; j = len(s2) -1
        li = []; lj = []
        pi, pj = 0,0
        lpi, lpj = pi, pj
        while i < len(s1) and j >= 0 and ((pi == 0 and pj == 0) or s1[i] == s2[j]):
            lpi, lpj = pi, pj
            li.append(s1[i])
            lj.insert(0, s2[j])
            i += 1
            j -= 1
            #if li == lj:return i, j+1
            if sorted(li).__eq__(sorted(lj)):
                #pi, pj = i, j+1
                return i, j+1
        if pi == len(s1) and lpi != 0:
            return lpi,lpj
        return pi, pj

    def preprocess(self, s1: str, s2: str):
        if s1[0] == s2[-1] or s1[-1] == s2[0]:
            self.s1 = s1
            self.s2 = s2
            return
        begin = 0
        while s1[begin] == s2[begin] and begin < len(s1):
            begin += 1
        end = len(s1)-1
        while s1[end] == s2[end] and end >= 0:
            end -= 1
        self.s1 = s1[begin: end+1]
        self.s2 = s2[begin: end+1]
        print("preprocess s1: {}, s2: {}".format(self.s1, self.s2))


    def precheck(self) ->bool:
        ds1 = {}
        ds2 = {}
        for i in range(len(self.s1)):
            if self.s1[i] not in ds1:
                ds1[self.s1[i]] = 1
            else:
                cnt = ds1.get(self.s1[i])
                ds1[self.s1[i]] = cnt+1
            if self.s2[i] not in ds2:
                ds2[self.s2[i]] = 1
            else:
                cnt = ds2.get(self.s2[i])
                ds2[self.s2[i]] = cnt+1
        ds1 = dict(sorted(ds1.items(), key=lambda kv: kv[0]))
        ds2 = dict(sorted(ds2.items(), key=lambda kv: kv[0]))
        if ds1 == ds2:return True
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):return False
        if s1 == s2: return True
        self.flag = False
        self.lastdiv = -1
        self.preprocess(s1, s2)
        if self.precheck():
            self.helper(0, len(self.s1), 0, len(self.s2))
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
s1 = "abcd"
s2 = "badc"
s1 = "cbcccccbbabcbac"
s2 = "bbccaccbcbcabcc"
s1 = "oatzzffqpnwcxhejzjsnpmkmzngneo"
s2 = "acegneonzmkmpnsjzjhxwnpqffzzto"
s1 = "abcd"
s2 = "dacb"
s1 = "abbbcbaaccacaacc"
s2 = "acaaaccabcabcbcb"

"bbbcbaaccacaacc"
"caaaccabcabcbcb"

"bbcbaaccacaacc"
"caaaccabcabcbc"

"acaacc"
"caaacc"

sol = Solution()
res = sol.isScramble(s1, s2)
print(res)

