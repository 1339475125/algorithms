#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
# 队列

class Solution:

    def LRU(self , operators , k ):
        # write code here
        # 队列
        cache = {}
        queque = []
        res = []
        for item in operators:
            if len(item) == 3:
                self.set(queque, cache, item[1], item[2], k)
            else:
                res.append(self.get(queque, cache, item[1]))
        return res
        
    def set(self, queque, cache, key, value, k):
        queque.append(key)
        cache[key] = value
        if len(queque) > k:
            pop_data = queque.pop(0)
            cache.pop(pop_data)
        return
    
    def get(self, queque, cache, key):
        if key in cache:
            queque.remove(key)
            queque.append(key)
            return cache.get(key)
        return -1


s = Solution()
operators, k = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
print(s.LRU(operators, k))
