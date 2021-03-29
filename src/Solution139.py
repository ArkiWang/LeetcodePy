class Solution:
    def helper(self, i: int, s: str, wordDict: [], mark: []):
        if i < len(s):
            for w in wordDict:
                if s[i: i+len(w)] == w and not mark[i+len(w)]:
                    mark[i+len(w)] = True
                    self.helper(i+len(w), s, wordDict, mark)

    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        mark = [False] * (len(s)+1)
        self.helper(0, s, wordDict, mark)
        return mark[-1]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
res = sol.wordBreak(s, wordDict)