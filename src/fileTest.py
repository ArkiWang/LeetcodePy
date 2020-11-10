from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums) and nums[i] == 0: i += 1
        interval = 0
        intervalList = []
        for j in range(i, len(nums)):
            if nums[j] == 0:
                interval += 1
            else:
                intervalList.append(interval)
                interval = 0
        if len(intervalList) > 0:
            intervalList.__delitem__(0)
        else:
            return False
        for i in range(len(intervalList)):
            if intervalList[i] < k:
                return False
        return True

solution = Solution()
nums = [1,0,0,0,1,0,0,1]
k = 2
res = solution.kLengthApart(nums, k)
print(res)
