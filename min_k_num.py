"""
给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组
"""

def get_k_min_data(nums, k):
    if k > len(nums):
        return None
    if not nums:
        return None
    res = quick_sort(nums)
    min_stack = res[:k]
    return min_stack


def quick_sort(nums):
    if not nums:
        return []
    item = nums[0]
    left = quick_sort([x for x in nums[1:] if x < item])
    right = quick_sort([x for x in nums[1:] if x >= item])
    return left + [item] + right

a = [1,3, 2, 4, 5,8,6, 7,9]
print(get_k_min_data(a, 8))