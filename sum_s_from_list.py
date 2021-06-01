"""
求一个数组中和为s的两个值，若多个取乘积最小的
"""


def get_sum_s_data(nums, target):
    if not nums:
        return None
    res = []
    tmp = 0
    reverse_nums = nums[::-1]
    if target > nums[0] + reverse_nums[0]:
        return None
    for i in range(1, len(nums)):
        for j in range(1, len(reverse_nums)/2):
            if nums[i] + reverse_nums[j] == target:
                if not tmp:
                    tmp = nums[i] * reverse_nums[j]
                    res.append((nums[i], reverse_nums[j]))
                else:
                    if tmp > nums[i] * reverse_nums[j]:
                        tmp = nums[i] * reverse_nums[j]
                        res.pop()
                        res.append((nums[i], reverse_nums[j]))
                break
    print(res)
    print(tmp)


nums = [1, 2, 3, 4, 5]
get_sum_s_data(nums, 5)