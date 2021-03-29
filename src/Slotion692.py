class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        dic = {}
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        dic = dict(sorted(dic.items(), key=lambda kv: kv[0]))
        print(dic)
        dic = dict(sorted(dic.items(), key=lambda kv: kv[1], reverse=True))
        print(dic)
        ans = []
        cnt = 0
        for key in dic.keys():
            if cnt < k:
                ans.append(key)
                cnt += 1

        return ans

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
sol = Solution()
res = sol.topKFrequent(words, k)
print(res)