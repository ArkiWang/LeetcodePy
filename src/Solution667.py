class Solution:
    def pair(self, original: [], n: int) -> []:
        l, u = original[:int((n+1) / 2)], original[int((n+1) / 2):]
        u = u[::-1]
        print("l {}".format(l))
        print("u {}".format(u))
        res = []
        for i in range(int(n / 2)):
            res.append(l[i])
            res.append(u[i])
        if n % 2 == 1: res.append(l[i+1])
        return res

    def constructArray(self, n: int, k: int) -> [int]:
        original = [i + 1 for i in range(n)]
        if k == 1:
            return original
        elif k == n-1:
            return self.pair(original, n)
        else:
            remain = n - k -1
            change = k + 1
            cl = self.pair(original[: change], change)
            rl = original[change:]
            print("cl {}".format(cl))
            print("rl {}".format(rl))
            return cl + rl

sol = Solution()
res = sol.constructArray(5, 2)
print(res)