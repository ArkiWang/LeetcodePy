class Solution:
    def sumSubarrayMins2(self, arr: [int]) -> int:
        minStack = []
        res, dot = 0, 0
        for i, y in enumerate(arr):
            cnt = 1
            while len(minStack) > 0 and minStack[-1][0] > y:
                x, c = minStack.pop()
                dot -= x*c
                cnt += c

            dot += y * cnt
            res += dot
            minStack.push(y, cnt)
        return res

    def sumSubarrayMins1(self, arr: [int]) -> int:
        n = len(arr)
        per, s = 0, 0
        for i in range(n-1, -1, -1):
            for j in range(n-i):
                if j == 0:
                    per = arr[i]
                elif arr[i+j] < per:
                    per = arr[i+j]
                s = (s + per)%(10**9+7)
        return s

    def sumSubarrayMins(self, A):
        MOD = 10 ** 9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD



arr = [3,1,2,4]
sol = Solution()
res = sol.sumSubarrayMins(arr)
print(res)