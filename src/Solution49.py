from copy import deepcopy
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        sorted_strs = {}
        for i, s in enumerate(strs):
            sorted_s = str(sorted(s))
            if sorted_s not in sorted_strs:
                sorted_strs[sorted_s] = [i]
            else:
                sorted_strs[sorted_s].append(i)
        #sorted_strs = dict(sorted(sorted_strs.items(), key=lambda kv:kv[1]))
        #print(sorted_strs)
        res = []
        for key in sorted_strs:
            pos_set = sorted_strs.get(key)
            tmp = []
            for i in pos_set:
                tmp.append(strs[i])
            res.append(tmp)
        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
res = sol.groupAnagrams(strs)
print(res)



