"""
单调栈
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 找下一个比他大的数字的下标减去当前的下标
        if not temperatures:
            return []
        res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j -i
        #             break
        stack = list()
        for key, value in enumerate(temperatures):     
            if stack:
                while stack and temperatures[stack[-1]] < value:
                    res[stack[-1]] = key - stack[-1]
                    stack.pop()
            stack.append(key)
            print(stack)
        return res