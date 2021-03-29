class Solution:
    def trap(self, height: [int]) -> int:
        n = len(height)
        l = [0]*(n+1)
        r = [0]*(n+1)
        for i in range(n):
            l[i+1] = max(l[i], height[i])
        for i in range(n-2, -1, -1):
            r[i] = max(r[i+1], height[i+1])
        print(l, r)
        ans = 0
        for i in range(n):
            h = min(l[i], r[i])
            if h > 0 and h > height[i]:
                ans += h - height[i]
        return ans
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
sol = Solution()
res = sol.trap(height)
print(res)

