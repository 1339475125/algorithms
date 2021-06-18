# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(1, left):
            pre = pre.next
        head = pre.next
        for i in range(left, right):
            nex = head.next
            head.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return dummy.next


link1 = ListNode(1)
link2 = ListNode(2)
link3 = ListNode(3)
link4 = ListNode(4)
link5 = ListNode(5)

link1.next = link2
link2.next = link3
link3.next = link4
link4.next = link5
s = Solution()
print(s.reverseBetween(link1, 2, 4))