
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
"""

def sub_list(nums):
    if not nums:
        return [[]]
    res = []
    for i in range(len(nums)):
        if not i:
            res.append([])
        else:
            data = get_data(nums, i)
            res.extend(data)
    res.append(nums)
    return res


def get_data(nums, i):
    data = []
    x = 0
    y = x + i
    while x < len(nums) or y <= len(nums):
        data.append(nums[x:y])
        x += 1
        y += 1
    return data


nums = [1, 2, 3]
print(sub_list(nums))