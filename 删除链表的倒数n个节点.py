class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        dummy = ListNode(0)
        dummy.next = head
        slow = head
        fast = head
        while(fast.next):
            while(n):
                n = n-1
                fast = fast.next
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
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
print(s.removeNthFromEnd(link1, 2))