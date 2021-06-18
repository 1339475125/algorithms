"""
由方法一可知，如果可以到达目标字符串，那么一定满足 转换不变性 和 可到达性。

可以用双指针来解决这个问题，对于 i， j 两个指针，分别让他们指向 start 和 end，
且保证 start[i] != 'X'，end[j] != 'X'。接下来开始移动指针，如果 start[i] != end[j]，
则不满足 转换不变性，如果 start[i] == 'L' 且 i < j，则不满足 可到达性。
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0
        m, n = len(start), len(end)
        start = start + '#'
        end = end + '#'
        while i < m or j < n:
            while i < m and start[i] == 'X': i += 1
            print(i)
            while j < n and end[j] == 'X': j += 1
            print(j)
            if start[i] != end[j]:
                return False
            if i < m:
                if start[i] == 'L' and i < j:
                    return False
                if start[i] == 'R' and i > j:
                    return False
            if i < m:
                i += 1
            if j < n:
                j += 1
        return True


s = Solution()
start = "RXXLRXRXL"
end = "XRLXXRRLX"
s.canTransform(start, end)