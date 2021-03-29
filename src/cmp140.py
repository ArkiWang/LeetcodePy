class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        #@lru_cache(None)
        def backtrack(index: int) -> [[str]]:
            if index == len(s):
                return [[]]
            ans = []
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breaks = backtrack(0)
        return [" ".join(words[::-1]) for words in breaks]


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
