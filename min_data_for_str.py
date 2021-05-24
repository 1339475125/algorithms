"""
字符串组成最小的数
"""

def get_min_number(numbers):
    if not numbers:
        return ""
    n = len(numbers)
    nums = [str(i) for i in numbers]
    for i in range(1, n):
        if nums[i] + nums[i -1] < nums[i-1] + nums[i]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
    return "".join(nums)

a = [3, 32, 321]
print(get_min_number(a))