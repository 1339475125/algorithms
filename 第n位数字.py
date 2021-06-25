import math

class Solution:
    def findNthDigit(self, n: int) -> int:
        if not n:
            return -1
        if n < 9:
            return n
        sum_n = 9
        index = 2
        while(sum_n + 9 * math.pow(10, index - 1) * index < n):
            sum_n += 9 * math.pow(10, index - 1) * index
            index = index + 1
        pos = n - sum_n #2
        i = math.pow(10, index-1) + pos /index # 10
        i1 = int(pos % index)
        if i1 !=0:
            for j in range(index -i1):
                i = i / 10
            return int(i % 10)

        else:
            return int((i-1) % 10)


s = Solution()
print(s.findNthDigit(1000)