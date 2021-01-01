from copy import deepcopy


class Solution:

    def dfs(self, i, edges: dict, mark: set, pos: set, vertexes: set):
        if len(edges) > 0 and i in edges and i not in mark:
            if i not in mark:
                mark.add(i)
                pos.add(i)
                if i in vertexes:vertexes.remove(i)
                for v in list(edges.get(i)):
                    self.dfs(v, edges, mark, pos, vertexes)


    def combine_pairs(self, pairs: [[int]]):
        edges = {}
        vertexes = set()
        for p in pairs:
            vertexes.add(p[0])
            vertexes.add(p[1])
            if p[0] not in edges:
                edges[p[0]] = {p[1]}
            else:
                edges[p[0]].add(p[1])
            if p[1] not in edges:
                edges[p[1]] = {p[0]}
            else:
                edges[p[1]].add(p[0])
        pos_list = []
        mark = set()
        print("v: ", vertexes)
        while len(vertexes) > 0:
            key = vertexes.pop()
            if key not in mark:
                pos = set()
                self.dfs(key, edges, mark, pos, vertexes)
                pos_list.append(list(deepcopy(pos)))
        print(pos_list)
        return pos_list

    def select_sort(self, pos:[], s:[]):
        pos_sort = []
        for i in range(len(s)):
            if i in pos:
                pos_sort.append(s[i])
        pos_sort.sort()
        for i in range(len(pos)):
            s[pos[i]] = pos_sort[i]
        return s


    def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
        pos_list = self.combine_pairs(pairs)
        s = list(s)
        for pos in pos_list:
            pos.sort()
            s = self.select_sort(pos, s)
        ss = ''
        for si in s:
            ss += si
        return ss


s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
s = "wiftyfgoqfohnzelum"
pairs = [[3,2],[6,2],[9,11],[2,3],[5,4],[2,2],[4,3],[9,3],[10,0],[4,16],[5,8],[14,5],[4,16],[17,1],[9,7],[12,9],[1,17],[16,7]]
s = "xwwbesrhlaoucciymqe"
pairs = [[12,5],[17,8],[0,8],[8,13],[16,10],[4,15],[11,12],[2,11],[14,7],[13,18],[1,10],[4,8],[2,17],[8,1],[15,13],[16,12],[16,18],[13,11],[12,0]]
sol = Solution()
res = sol.smallestStringWithSwaps(s, pairs)
print(res)