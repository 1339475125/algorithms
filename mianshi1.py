"""
如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
"""


def get_min_data(num):
    if not num:
        return 0
    num_5 = int(num / 5)
    num = num - num_5 * 5
    num_3 = int(num / 3)
    num -= num_3 * 3
    return num_5 + num_3 + num
    

if __name__ == "__main__":
    num = 11
    print(get_min_data(11))
