class Solution:
    res_list = []
    def find_all(self, s: str, p:str) -> {}:
        low = 0
        res = set()
        while low < len(s):
            low = s.find(p, low)
            if low == -1:
                return res
            res.add(low)
            low += 1
        return res

    def generator(self, i, s, dic, res=''):
        if i < len(s):
            if i in dic:
                for w in dic[i]:
                    if i+len(w) <= len(s):
                        self.generator(i+len(w), s, dic, res+w+' ')
        else:
            print(res[:-1])
            self.res_list.append(res[:-1])

    def precheck(self, s: str, wordDict: []):
        i = 0
        wordSet = set()
        while i < len(s):
            for word in wordDict:
                if s[i: i+len(word)] == word:
                    wordSet.add(word)
                    i += len(word)
                    break



    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        dic = {}
        for word in wordDict:
            lows = self.find_all(s, word)
            for low in lows:
                if low not in dic:
                    dic[low] = {word}
                else:
                    dic[low].add(word)
        print(len(dic))
        self.res_list = []
        self.generator(0, s, dic)
        return self.res_list

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
