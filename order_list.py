"""
调整数组顺序使奇数位于偶数前面
"""
import copy


def re_order_array(nums):
    #  奇数(O(N))
    odd_cnt = 0 
    for x in nums:
        if not (x % 2):
            odd_cnt = odd_cnt +1
    copy_list = copy.deepcopy(nums)
    i = 0
    j = odd_cnt
    for x in copy_list:
        if (x % 2) == 1: 
            nums[i] = x
            i = i +1
        else:
            nums[j+1] = x
            j = j + 1
    return nums


def maopao(nums):
    N = len(nums)
    for i in range(N):
        for j in range(i):
            if is_even(nums[j]) and not is_even(nums[j + 1]):
                swap(nums, j, j+ 1)
    return nums

def is_even(x):
    return x%2==0

def swap(nums, i, j):
    nums[i] = nums[j]


if __name__ == "__main__":
    nums = [1, 2, 3, 4,5]
    print(re_order_array(nums))
    print(maopao(nums))