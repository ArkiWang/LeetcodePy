from numpy import mean, inf


class Solution:
    def minMoves2(self, nums: [int]) -> int:
        nums = sorted(nums)
        Mean = nums[int(len(nums)/2)]
        res = 0
        for n in nums:
            res += abs(n - Mean)
        return res

nums = [1,0,0,8,6]
#nums = [203125577,-349566234,230332704,48321315,66379082,386516853,50986744,-250908656,-425653504,-212123143]
sol = Solution()
res = sol.minMoves2(nums)
print(res)