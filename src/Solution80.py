class Solution:
    def remove_from(self, start, nums):
        key = nums[start]
        end = start
        for i in range(start, len(nums)):
            if nums[i] == key:
                end = i
        if end+1 < len(nums):
            nums = nums[:start]+nums[end+1:]
        else:
            nums = nums[:start]
        return nums, end - start
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) < 1:return len(nums)
        now = nums[0]
        cnt, i = 1, 1
        while i < len(nums):
            if i < len(nums) and nums[i] == now:
                cnt += 1
            else:
                now = nums[i]
                cnt = 1
            if cnt > 2:
                nums, rems = self.remove_from(i, nums)
                i -= rems
            i += 1
        print(nums)
        return len(nums)

nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
sol = Solution()
res = sol.removeDuplicates(nums)
print(res)
