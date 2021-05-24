"""
把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。例如 6、8 都是丑数，但 14 不是，因为它包含因子 7。习惯上我们把 1 当做是第一个丑数。求按从小到大的顺序的第 N 个丑数。
"""


def get_ugly_number(n):
    if n<=6:
        return n
    
    dp = [0] * n
    dp[0] = 1
    i2 = 0
    i3 = 0
    i5 = 0
    for i in range(1, n):
        next2 = dp[i2] * 2
        next3 = dp[i3] * 3
        next5 = dp[i5] * 5
        dp[i] = min(next2, min(next3, next5))
        if dp[i] == next2:
            i2 += i2

        if dp[i] == next3:
            i3 += i3
        
        if dp[i] == next5:
            i5 += i5
    print(dp)



def get_ugly_number1(n):
    if n <= 0:
        return 0
    data = 0
    count = 0
    while(count < n):
        data = data + 1
        tmp = data
        while (tmp % 2) == 0:
            tmp = tmp / 2
        while (tmp % 3) == 0:
            tmp = tmp / 3
        while (tmp % 5) == 0:
            tmp = tmp / 5
        if tmp == 1:
            count = count + 1 
    print(data)

get_ugly_number(10)
get_ugly_number1(10)