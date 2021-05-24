"""
数字序列中的某一位数字
"""


def get_index_num(str, n):
    if n < 0:
        return -1
    for k, s in enumerate(str):
        if k == n:
            return s
    

print(get_index_num("1231414141414", 3))