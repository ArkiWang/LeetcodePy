class Solution:
    mark = set()
    flag = False
    def handler(self, arr: [int], i: int):
        if arr[i] != 0 and self.flag is not True:
            self.mark.add(i)
            if self.flag is not True and i + arr[i] not in self.mark and i + arr[i] >= 0 and i + arr[i] < len(arr):
                self.handler(arr, i + arr[i])
            if self.flag is not True and i - arr[i] not in self.mark and i - arr[i] >= 0 and i - arr[i] < len(arr):
                self.handler(arr, i - arr[i])
        else:
            self.flag = True

    def canReach(self, arr: [int], start: int) -> bool:
        self.mark = set()
        self.flag = False
        self.handler(arr, start)
        return self.flag

arr = [4,2,3,0,3,1,2]
start = 5
arr = [3,0,2,1,2]
start = 2
sol = Solution()
res = sol.canReach(arr, start)
print(res)