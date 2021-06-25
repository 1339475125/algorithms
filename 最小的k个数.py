# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or not k:
            return []
        if len(tinput) < k:
            return []
        stack = []
        while(len(stack) < k):
            stack.append(tinput[0])
            index = 0
            for i in range(len(tinput)):
                if tinput[i] < stack[-1]:
                    stack.pop()
                    stack.append(tinput[i])
                    index = i
            tinput.pop(index)
        return stack

    
    
    
    
    
    
    
    