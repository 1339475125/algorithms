


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    size = len(nums)
    mid = int(size / 2)
    left = nums[0:mid]
    right = nums[mid+1:]
    merge_sort(left)
    merge_sort(right)
    print(left, right, mid)
    return left + [nums[mid]] + right


def merge(nums):
    print(nums)
    res = [0] * len(nums)
    mid = int(len(nums) / 2)
    print(mid)
    res[mid] = nums[mid]
    left = nums[:mid]
    right = nums[mid:]
    p1 = 0
    p2 = 0
    while p1 < mid or p2 < mid:
        if left[p1] < right[p2]:
            res.append(left[p1])
            p1 += 1 
        else:
            res.append(right[p2])
            p2 += 1
    while p1 <= mid:
        res.extend(left[p1:])
    while p2 <= mid:
        res.extend(right[p2:])
    return res


if __name__ == "__main__":
    nums = [4, 2, 3, 1, 5, 0]
    res = merge_sort(nums)
    print(merge(res))