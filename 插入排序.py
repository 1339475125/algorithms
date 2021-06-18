"""
插入排序
"""

def sort_insert(nums):
    for i in range(1, len(nums)):
        for j in range(0, i):
            print("11111111", i, j , nums[i], nums[j])
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == "__main__":
    nums = [5, 2, 4, 3, 1]
    print(sort_insert(nums))