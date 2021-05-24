"""
打印从1到最大的n位数
1-3 就是1 -999
因为n可能很大用字符串
使用回溯法
"""


def print_1_to_maxof_ndigits(n):
    if n <= 0:
        return -1
    number = ['0'] * n
    while increamnet(number) is False:
        print_number(number)


def increamnet(number):
    is_overflow = False
    is_takeover = False
    
    length = len(number)
    n = length - 1

    while n >= 0:
        nsum = int(number[n]) + is_takeover

        if n == length -1:
            nsum = nsum +1

        if nsum == 10:
            if n == 0:
                is_overflow = True
                return is_overflow

            else:
                is_takeover = True
                number[n] = '0'
        else:
            number[n] = str(nsum)
            break
        n = n -1
    return is_overflow


def print_number(number):
    for i in range(len(number)):
        if number[i] !='0':
            print(''.join(number[i:]))
            break


if  __name__ == "__main__":
    print_1_to_maxof_ndigits(2)