"""
复制每一个节点，并且将这个节点插入到每个节点的下一个
设置没个节点的random
分离链表，生层新的链表
"""
# Definition for a Node.
class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = ListNode(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点



link1 = ListNode(1)
link2 = ListNode(2)
link3 = ListNode(3)
link4 = ListNode(4)
link5 = ListNode(5)

link1.next = link2
link1.random = link5
link2.next = link3
link2.random  = link1
link3.next = link4
link3.random = link4
link4.next = link5
link4.random = link3
s = Solution()
print(s.copyRandomList(link1))


