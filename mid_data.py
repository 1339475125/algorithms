"""
中位数
"""
import math
import heapq

class Solution:

    def __init__(self):
        self.nums = []

    def Insert(self, num):
        heapq.heappush(self.nums, num)
    
    def GetMedian(self):
        mid = math.ceil(len(self.nums)/ 2)
        return (heapq.nlargest(mid, self.nums)[-1] + heapq.nsmallest(mid, self.nums)[-1]) / 2.0

s = Solution()
s.Insert(1)
s.Insert(2)
s.Insert(3)
s.Insert(4)
print(s.GetMedian())