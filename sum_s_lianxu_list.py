"""
和为s的连续序列
"""


def get_sum_s_data(sum):
    ret = []
    start = 1
    end = 2
    curSum = 3
    while end < sum:
        if curSum > sum:
            curSum -= start
            start = start + 1
        elif curSum < sum:
            end += 1
            curSum += end
        else:
            res = []
            for i in range(start, end+1):
                res.append(i)
            ret.append(res)
            curSum -= start
            start += 1
            end += 1
            curSum += end
    return ret


print(get_sum_s_data(100))
