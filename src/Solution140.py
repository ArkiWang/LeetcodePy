class Solution:
    def helper(self, i: int, s: str, wordDict: [], mark: []):
        if i < len(s):
            for w in wordDict:
                if s[i: i + len(w)] == w and not mark[i + len(w)]:
                    mark[i + len(w)] = True
                    self.helper(i + len(w), s, wordDict, mark)

    def check(self, s: str, wordDict: [str]) -> bool:
        mark = [False] * (len(s) + 1)
        self.helper(0, s, wordDict, mark)
        return mark[-1]

    res_list = None
    def helper(self, i: int, s: str, wordDict: [str], res=''):
        if i < len(s):
            for word in wordDict:
                if s.find(word, i, len(s)) == i:
                    self.helper(i+len(word), s, wordDict, res+word+' ')
        elif i == len(s):
            self.res_list.add(res[:-1])


    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        if self.check(s, wordDict):
            self.res_list = set()
            self.helper(0, s, wordDict, '')
            return self.res_list
        else:
            return []


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
print('over')
