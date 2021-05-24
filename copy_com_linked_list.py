"""
复制复杂列表
"""

class Solution:
    def clone(self, pHead):
        if not pHead:
            return
        
        kk =pHead
        while kk:
            node = pHead.value
            node.next = kk.next
            kk.next = node
            kk = node.next

        kk = pHead
        while kk:
            if kk.random:
                kk.next.random = kk.random
            kk = kk.next.next

        kk = pHead
        nn = pHead.next
        while kk:
            kk.next = kk.next.next
            if nn.next:
                nn.next = nn.next.next
                nn = nn.next
            kk = kk.next
        return nn

