"""
列表中最小的k个值
"""


def get_min_k_data(nums, k):
    """
    排序, 分片
    """
    if not nums:
        return []
    res = sort_data(nums)
    print(res)
    return res[:k]


def sort_data(nums):
    # 排序
    left_list = []
    right_list = []
    if not nums:
        return nums
    data = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < data:
            left_list.append(nums[i])
        else:
            right_list.append(nums[i])
    return (sort_data(left_list) + [data] + sort_data(right_list))
    



if __name__ == "__main__":
    nums = [1, 4, 2, 3, 5]
    k = 2
    print(get_min_k_data(nums, k))
