from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if 1 not in nums:
            return 1
        size = len(nums)
        for i in range(size):
            if nums[i] <= 0 or nums[i] > size:
                nums[i] = 1
        for i in range(size):
            a = abs(nums[i]) - 1 # 值为2那就是第1位上的数字出现了
            nums[a] = -abs(nums[a])
            print(nums)
        for i in range(size):
            if nums[i]>0:
                return i+1
        print(nums)
        return size+1


s = Solution()
nums = [2, 1, 2, 4, 3, -1, -3, 5, 9]
print(s.firstMissingPositive(nums))