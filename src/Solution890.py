from copy import deepcopy
class Solution:
    def check(self, word, pattern):
        if len(word) != len(pattern):
            return False
        pset, wset = [], []
        for i in range(len(word)):
            if not pset.__contains__(pattern[i]) and not wset.__contains__(word[i]):
                pset.append(pattern[i])
                wset.append(word[i])
        dic = {}
        for i in range((len(pset))):
            dic[pset[i]] = wset[i]

        res = ''
        for i in range(len(pattern)):
            if pattern[i] in dic:
                res += dic.get(pattern[i])
        if res == word:return True
        return False


    def findAndReplacePattern(self, words: [str], pattern: str) -> [str]:
        res = []
        for word in words:
            if self.check(word, pattern):
                res.append(word)
        return res


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
sol = Solution()
res = sol.findAndReplacePattern(words, pattern)
print(res)


