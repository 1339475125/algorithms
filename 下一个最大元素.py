"""
栈
通过Stack、HashMap解决

先遍历大数组nums2，首先将第一个元素入栈；
继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = {}
        for n in nums2:
            while stack and stack[-1] < n:
                res[stack.pop()] = n 
            stack.append(n)
            print(stack)
        return [res.get(x, -1) for x in nums1]