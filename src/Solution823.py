class Solution:
    def numFactoredBinaryTrees(self, arr: [int]) -> int:
        res = {}
        arr = sorted(arr)
        for i, e in enumerate(arr):
            res[arr[i]] = 1

        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i]%arr[j] == 0 and int(arr[i]/arr[j]) in arr:
                    cnt1 = res.get(arr[j])
                    cnt2 = res.get(int(arr[i]/arr[j]))
                    res[arr[i]] = (res[arr[i]] + cnt1 * cnt2)%(10 ** 9 + 7)

        print(res)
        sum = 0
        for key in res.keys():
            sum += res.get(key)

        return sum

A = [2, 4, 5, 10]
A = [46,144,5040,4488,544,380,4410,34,11,5,3063808,5550,34496,12,540,28,18,13,2,1056,32710656,31,91872,23,26,240,18720,33,49,4,38,37,1457,3,799,557568,32,1400,47,10,20774,1296,9,21,92928,8704,29,2162,22,1883700,49588,1078,36,44,352,546,19,523370496,476,24,6000,42,30,8,16262400,61600,41,24150,1968,7056,7,35,16,87,20,2730,11616,10912,690,150,25,6,14,1689120,43,3128,27,197472,45,15,585,21645,39,40,2205,17,48,136]
sol = Solution()
res = sol.numFactoredBinaryTrees(A)
print(res)




