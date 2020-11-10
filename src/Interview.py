from typing import List
import numpy as np

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ndic = {}
        for i in range(len(numbers)):
            if target-numbers[i] in ndic:
                f = ndic.get(target-numbers[i])
                return [f+1,i+1]
            if numbers[i] not in ndic:
                ndic[numbers[i]] = i
        return [-1,-1]

   # 3 arrays which length equals k
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        dp = np.zeros((len(nums),3),int)
        sum = 0;cnt = 0



s=Solution()
numbers=[2, 7, 11, 15]
res=s.twoSum([2, 7, 11, 15],9)
print(res)

i : int
j = 1.3
i = j
print(i)