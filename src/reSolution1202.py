import collections
import heapq
class Solution:
    def union_helper(self, dic, mark, key, lp0):
        if lp0 in dic:
            vset = dic.get(lp0)
            dic[key] = dic[key].union(vset)
            for v in vset:
                mark[v] = key
            dic.__delitem__(lp0)

    def union(self, pairs: [[int]], length: int, s):
        dic = {}
        mark = [i for i in range(length)]
        for p in pairs:
            lp0 , lp1 = mark[p[0]], mark[p[1]]
            key = min(mark[p[0]], mark[p[1]])
            if key not in dic:
                dic[key] = {p[0], p[1]}
            else:
                dic[key].add(p[0])
                dic[key].add(p[1])

            if lp0 != key:
                self.union_helper(dic, mark, key, lp0)
                mark[p[0]] = key
            if lp1 != key:
                self.union_helper(dic, mark, key, lp1)
                mark[p[1]] = key

        dic = {}
        for v,k in enumerate(mark):
            if k not in dic:
                dic[k] = [s[v]]
            else:
                heapq.heappush(dic[k], s[v])

        print(dic)
        ss = ''
        for i in range(length):
            ss += heapq.heappop(dic[mark[i]])
        return ss



    def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
        #查并集
        p = {i:i for i in range(len(s))}
        def f(x: int):
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)
            print(p)
        # 合并可交换位置
        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            #d[j].append(i)
            heapq.heappush(d[j], i)
        print(d)
        # 排序
        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)
            for i, c in zip(q, t):
                ans[i] = c

        return ''.join(ans)



s = "wiftyfgoqfohnzelum"
pairs = [[3,2],[6,2],[9,11],[2,3],[5,4],[2,2],[4,3],[9,3],[10,0],[4,16],[5,8],[14,5],[4,16],[17,1],[9,7],[12,9],[1,17],[16,7]]

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
s = "cba"
pairs = [[0,1],[1,2]]

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
s = "fqtvkfkt"
pairs = [[2,4],[5,7],[1,0],[0,0],[4,7],[0,3],[4,1],[1,3]]
s = "xwwbesrhlaoucciymqe"
pairs = [[12,5],[17,8],[0,8],[8,13],[16,10],[4,15],[11,12],[2,11],[14,7],[13,18],[1,10],[4,8],[2,17],[8,1],[15,13],[16,12],[16,18],[13,11],[12,0]]
s = "qdwyt"
pairs = [[2,3],[3,2],[0,1],[4,0],[3,2]]
sol = Solution()
res = sol.smallestStringWithSwaps(s, pairs)
print(res)