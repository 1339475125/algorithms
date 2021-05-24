"""
连续子数组的最大和---动态规划、分治算法
"""

class Solution:

    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)

nums = [-2, 1, 13, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(nums))