class Solution:
    def canArrange(self, arr: [int], k: int) -> bool:
        r = [0] * k
        for a in arr:
            r[a % k] += 1
        for i in range(1, int(k/2)+1):
            if r[i] != r[k-i]:
                return False
            if k % 2 == 0 and i == int(k/2) and r[i] % 2 != 0:
                return False
        return True

arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
arr = [-10, 10]
k = 2
arr = [3,8,7,2]
k = 10
arr = [8,6,3,3]
k = 5
arr = [-1,-1,-1,-1,2,2,-2,-2]
k = 3
sol = Solution()
res = sol.canArrange(arr, k)
print(res)