"""
从 1 到 n 整数中 1 出现的次数
"""

def number_of_1_between_n(n):
    count = 0
    if n < 1:
        return count
    base = 1
    round = n
    while round > 0:
        weight = round % 10
        round = int(round / 10)
        print(round)
        count = count + round * base
        if weight == 1:
            count = count + (n % base) +1
        elif weight > 1:
            count += base
        base *= 10
    return count


n = 13
print(number_of_1_between_n(n))
