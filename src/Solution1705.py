import heapq
class Solution:
    def eatenApples(self, apples: [int], days: [int]) -> int:
        n = len(apples)
        max_days = 0
        h = []
        for i in range(n):
            max_days = max(max_days, i+days[i])
            heapq.heappush(h, (i+days[i], i, apples[i]))

        ans, min_rot, jeat = 0, 0, -1
        for i in range(max_days):
           # print("solve {} day".format(i))
            rot, begin, appnum = -1, -1, 0
            while h and (rot <= i or begin > i):
                rot, begin, appnum = heapq.heappop(h)
            print(begin, rot, appnum, i)
            if appnum > 1 and begin > i:
                heapq.heappush(h, (rot, begin, appnum - 1))
            if begin <= i and i < rot and appnum > 0:
                ans += 1
            '''
            jeat = -1
            for j in range(n):
                if apples[j] > 0 and i >= j and i < j + days[j] and (jeat == -1 or (min_rot > j + days[j])):
                    jeat = j
                    min_rot = j + days[j]
            if jeat >= 0 and apples[jeat] > 0 and i >= jeat and i < jeat + days[jeat]:
                apples[jeat] -= 1
                ans += 1
            '''
            #print(apples)
        return ans


apples = [3,1,1,0,0,2]
days = [3,1,1,0,0,2]
apples = [2,1,10]
days = [2,10,1]
apples = [0,47,47,0,27,11,24,2,0,0,32,12,34,24,40,28,35,16,0,38,0,0,30,17,11,0,0,47,0,33,27,7,43,0,0,43,41,10,35,27,43,8,0,0,10,5,3,0,1,24,17,0,17,0,0,22,41,35,0,10,16,8,10,17,0,38,35,18,6,29,9,0,14,11,0,0,43,14,17,3,6,4,2,44,6,18,26,0,23,11,37,37,1,47]
days = [0,19,68,0,37,17,35,3,0,0,17,23,2,23,25,24,51,27,0,41,0,0,51,29,21,0,0,60,0,33,50,4,7,0,0,16,77,4,44,17,65,7,0,0,3,4,3,0,1,24,1,0,22,0,0,41,62,39,0,20,3,3,10,16,0,71,53,32,8,31,14,0,15,5,0,0,15,9,7,4,3,5,3,82,5,16,25,0,3,5,57,34,2,73]
apples = [1,2,3,5,2]
days = [3,2,1,4,2]
sol = Solution()
res = sol.eatenApples(apples, days)
print(res)
