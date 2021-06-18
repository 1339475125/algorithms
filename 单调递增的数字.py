class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 从右向左扫描数字，若发现当前的数字比左边的小，则把左边的减一，右边的变成9
        snum = list(str(n))
        nine = len(snum)
        for i in range(len(snum) - 1, 0, -1):
            if snum[i] < snum[i-1]:
                snum[i-1] = str(int(snum[i-1]) -1)
                
                nine = i
        snum[nine:] = ['9'] * (len(snum)-nine)
        return int(''.join(snum))
        