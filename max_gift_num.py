"""
在一个 m*n 的棋盘的每一个格都放有一个礼物，每个礼物都有一定价值（大于 0）。从左上角开始拿礼物，每次向右或向下移动一格，直到右下角结束。给定一个棋盘，求拿到礼物的最大价值。例如，对于如下棋盘
"""


def get_max_gift_data(nums):
    if not nums:
        return 0
    if len(nums)==1 and len(nums[0])==1:
        return nums[0][0]
    size  = len(nums[0])
    dp = [0] * size
    for item in nums:
        dp[0] += item[0]
        for i in range(1, size):
            dp[i] = max(dp[i], dp[i-1]) + item[i]
    print(dp)


nums = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]]
get_max_gift_data(nums)
