import numpy as np
import functools
class Solution:
    def getfirends(self,i :int, friendsalllevel: set , ids: [], level: int, friends: [[int]]) ->[]:
        if i < level:
            tmp = set()
            for id in ids:
                for f in friends[id]:
                    if f not in friendsalllevel:
                        tmp.add(f)
                        friendsalllevel.add(f)
            return self.getfirends(i+1, friendsalllevel, list(tmp), level, friends)
        else:
            return ids

    def watchedVideosByFriends(self, watchedVideos: [[str]], friends: [[int]], id: int, level: int) -> [str]:
        friendsalllevel= set()
        friendsalllevel.add(id)
        fids = [id]
        fids = self.getfirends(0, friendsalllevel, fids, level, friends)
        print(fids)
        fvs = {}
        for fid in fids:
            for wv in watchedVideos[fid]:
                if wv not in fvs:
                    fvs[wv] = 1
                else:
                    cnt = fvs.get(wv)
                    fvs[wv] = cnt + 1
        fvs = dict(sorted(fvs.items(), key=lambda kv:kv[0]))
        fvs = dict(sorted(fvs.items(), key=lambda kv:kv[1]))
        print(fvs)
        return list(fvs.keys())

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2

watchedVideos = [["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]]
friends = [[1],[0]]
id = 0
level = 1
sol = Solution()
res = sol.watchedVideosByFriends(watchedVideos=watchedVideos, friends=friends, id=id, level=level)
print(res)



