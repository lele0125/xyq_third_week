class Solution:
    def permuteUnique(self, nums):
        if not nums or len(nums) == 1: return [nums]
        res = []
        cur = []
        l = len(nums)

        def backtrace(nums):
            if not nums:
                res.append(cur[:])
                return

            for i in range(len(nums)):
                cur.append(nums[i])
                backtrace(nums[:i] + nums[i + 1:])
                cur.pop()

        backtrace(nums)
        return res