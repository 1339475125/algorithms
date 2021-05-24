"""
数组中重复的数字
时间复杂度O(N), 空间复杂度O(1)
"""

def dup(nums):
    if not nums:
        return None
    for i in range(len(nums)):
        while(nums[i] != i):
            if nums[i]== nums[nums[i]]:
                return nums[i]
            swap(nums, i, nums[i])
            print(nums)
        swap(nums, i, nums[i])
        return None



def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


if __name__ == "__main__":
    nums = [2, 3, 4, 1, 2]
    print(dup(nums))



        