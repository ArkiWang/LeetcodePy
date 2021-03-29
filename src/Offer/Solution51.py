
class Solution:
    res = 0
    def margin(self, nums:[], low, mid, high):
        m = []
        res = 0
        i, j = low, mid+1
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                m.append(nums[i])
                i += 1
            else:
                self.res += mid-i+1
                m.append(nums[j])
                j += 1
        while i <= mid:
            m.append(nums[i])
            i += 1
        while j <= high:
            m.append(nums[j])
            j += 1
        nums[low: high+1] = m[:]
        return res


    def sort(self, nums: [int], low: int, high: int):
        if low < high:
            mid = int((low + high)/2)
            self.sort(nums, low, mid)
            self.sort(nums, mid+1, high)
            self.margin(nums, low, mid, high)


    def reversePairs(self, nums: [int]) -> int:
        self.res = 0
        self.sort(nums, 0, len(nums)-1)
        return self.res

nums = [7,5,6,4]
nums = [1,3,2,3,1]
nums = [1,1,-1,-1,-1,1]
sol = Solution()
res = sol.reversePairs(nums)
print(res)