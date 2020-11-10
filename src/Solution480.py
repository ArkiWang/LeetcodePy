from copy import deepcopy
from math import ceil
from typing import List


class Solution:
    def getMid(self, nums: list, k :int) -> int:
        if k <= 0:
            return -1
        if k%2==0:
            return (nums[int(k/2)-1]+nums[int(k/2)])/2
        else:
            return nums[int(k/2)]


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        nowlist = []
        for i in range(len(nums)-k+1):
            if i == 0:
                for j in range(k):
                    nowlist.append(nums[j])
                nowlist.sort()
                mid = self.getMid(nowlist,k)
                res.append(mid)
            else:
                print(nowlist, nums[i-1])
                nowlist.remove(nums[i-1])
                for j in range(k):
                    if j >= len(nowlist):
                        nowlist.append(nums[i+k-1])
                        break
                    elif nowlist[j]>nums[i+k-1]:
                        nowlist.insert(j,nums[i+k-1])
                        break
                mid = self.getMid(nowlist,k)
                res.append(mid)
        return res

solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = solution.medianSlidingWindow(nums, k)
print(res)
