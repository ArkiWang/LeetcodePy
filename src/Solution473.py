from copy import deepcopy
class Solution:
    his = []
    flag = False
    def handler(self, i: int, nums: [], l, res: [0, 0, 0, 0]):
        if i < len(nums) and not self.flag:
            res = sorted(res)
            for j in range(4):
                if res[j] + nums[i] <= l:
                    res[j] += nums[i]
                    if not self.his.__contains__(res) and not self.flag:
                        self.his.append(deepcopy(res))
                        self.handler(i+1, nums, l, res)
                    res[j] -= nums[i]
        else:
            self.flag = True
    def makesquare(self, nums: [int]) -> bool:
        c = sum(nums)
        if c % 4 != 0 or len(nums)<4:
            return False
        l = int(c / 4)
        for n in nums:
            if n > l:
                return False
        nums = sorted(nums)[::-1]
        self.his = []
        self.flag = False
        self.handler(0, nums, l, [0, 0, 0, 0])
        return self.flag

nums = [1,1,2,2,2]
nums = [3,3,3,3,4]
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
#nums = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
sol = Solution()
res = sol.makesquare(nums)
print(res)
