import numpy as np
class Solution:
    def partitionDisjoint(self, A: []) -> int:
        if A == None or len(A) < 1:return -1
        #max[i] the max number in 0..i
        max = [0]*len(A)
        for i in range(len(A)):
            if i == 0:
                max[i] = A[i]
            elif A[i] > max[i - 1]:
                max[i] = A[i]
            else:
                max[i] = max[i-1]
        #min[i] the min number in i..len-1
        min = [0]*len(A)
        for i in range(len(A)-1, -1, -1):
            if i == len(A)-1:
                min[i] = A[i]
            elif A[i] < min[i+1]:
                min[i] = A[i]
            else:
                min[i] = min[i+1]
        for i in range(0, len(A)-1):
            if max[i] <= min[i+1]:
                return i+1
        return -1
    
    def partitionDisjoint_test(self, A: []) -> int:
        if A == None or len(A) < 1:return -1
        for i in range(1, len(A)):
            if np.max(A[:i]) <= np.min(A[i:]):
                return i
        return -1

sol = Solution()
A = [1,1,1,0,6,12]
print(sol.partitionDisjoint(A))

            
            