# -*- coding:utf-8 -*-
"""
旋转数组的最小数字 ************
用二分法，复杂度是O(log2n)
l: low
m:mid
h:hight
"""

def min_number_in_rotate_array(nums):
    if not nums:
        return 0
    l, h = 0, len(nums) -1
    while(l<h):
        m = int(l + (h-l) / 2)
        if nums[l] == nums[h] and nums[h] == nums[m]:
            return min_number(nums, l, h)
        elif nums[m] <= nums[h]:
            h =m
        else:
            l = m + 1
    print(nums[l])
    return nums[l]


def min_number(nums, l, h):
    for i in range(l, h):
        if nums[i] > nums[i + 1]:
            return nums[i + 1]
        return nums[l]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5,1, 1, 2, 3]
    nums1 = [2, 2, 2, 0, 2, 2]
    min_number_in_rotate_array(nums)
    min_number_in_rotate_array(nums1)