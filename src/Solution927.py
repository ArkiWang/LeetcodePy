import numpy as np
class Solution:
    def threeEqualParts(self, A: [int]) -> [int]:
        total_ones_number = np.sum(A)
        if total_ones_number == 0:
            if len(A) > 2:
                return [0, 2]
            else:
                return [-1, -1]
        if total_ones_number%3 != 0: return [-1, -1]
        ones_per_block = total_ones_number / 3
        tile_zeros_number = 0
        cnt = 0
        i = len(A) - 1
        while i >= 0 and A[i] == 0:
            i -= 1
            tile_zeros_number += 1

        for i in range(len(A)-1-tile_zeros_number, -1, -1):
            if A[i] == 1:
                cnt += 1
                if cnt == ones_per_block:
                    pos = i
                    break
        l3 = pos; h3 = len(A)-1
        pos -= (tile_zeros_number+1)
        while pos >= 0 and A[pos] == 0:
            pos -= 1
            l3 -= 1
        h2 = pos + tile_zeros_number;cnt = 0
        for i in range(pos, -1, -1):
            if A[i] == 1:
                cnt += 1
                if cnt == ones_per_block:
                    pos = i
                    break
        if cnt < ones_per_block: return [-1, -1]
        l2 = pos
        pos -= tile_zeros_number
        while pos-1 >= 0 and A[pos-1] == 0:
            pos -= 1
            l2 -= 1
        h1 = pos - 1 + tile_zeros_number
        cnt = 0
        for i in range(pos-1, -1, -1):
            if A[i] == 1:
                cnt += 1
                if cnt == ones_per_block:
                    pos = i
                    break
        if cnt < ones_per_block: return [-1, -1]
        l1 = pos
        print(A)
        print(A[l1: h1+1])
        print(A[l2: h2+1])
        print(A[l3:])
        s1 = self.getnum(A[l1: h1+1])
        s2 = self.getnum(A[l2: h2+1])
        s3 = self.getnum(A[l3:])
        if  s1 == s2 and s2 == s3:
            return [h1, l3]
        return [-1, -1]

    def getnum(self, A: [])->int:
        sum = 0
        for a in A:
            sum = sum*2 + a
        return sum


    def threeEqualParts2(self, A: [int]) -> [int]:
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i, len(A)):
                if i == j:
                    dp[i][j] = A[i]
                else:
                    dp[i][j] = dp[i][j-1]*2 + A[j]
        for i in range(len(A)):
            for j in range(i+2, len(A)):
                if dp[0][i] == dp[i+1][j-1] and dp[0][i] == dp[j][-1]:
                    return [i, j]
        return [-1, -1]

    def threeEqualParts_test(self, A: [int]) -> [int]:
        front = [0] * len(A)
        rear = [0] * len(A)
        for i in range(len(A)):
            if i == 0:
                front[i] = A[i]
            else:
                front[i] = front[i-1]*2 + A[i]
        for i in range(len(A)-1, -1, -1):
            if i == len(A)-1:
                rear[i] = A[i]
            else:
                rear[i] = A[i]*pow(2,len(A)-1-i) + rear[i+1]
        '''
         for i in range(len(A)):
            for j in range(i+2, len(A)):
                if front[i] == rear[j]:
                    tmp = 0
                    for k in range(i+1, j):
                        tmp = tmp*2 + A[k]
                    if tmp == front[i]:
                        return [i, j]
        '''
        dr = {}
        for i, r in enumerate(rear):
            if r not in dr:
                dr[r] = [i]
            else:
                rl = dr.get(r)
                rl.append(i)
        for i, f in enumerate(front):
            if f in dr:
                rl = dr.get(f)
                for j in rl:
                    if j > i+1:
                        tmp = 0
                        for k in range(i + 1, j):
                            tmp = tmp * 2 + A[k]
                        if tmp == front[i]:
                            return [i, j]
        return [-1, -1]


sol = Solution()
A = [1,0,1,0,1]
#A = [1,1,0,1,1]
A = [1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]
res = sol.threeEqualParts(A)
print(res)
res = sol.threeEqualParts2(A)
print(res)