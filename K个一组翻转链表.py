# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = ListNode(0)
        curr = head 
        next = None

        if not head:
            return None
        if k == 1:
            return head

        size = 0
        while(head):
            head = head.next
            size = size + 1

        for i in range(int(size/k)):
            for j in range(k-1):
                # import pdb
                # pdb.set_trace()
                next = curr.next
                curr.next = next.next
                next.next = prev.next
                prev.next = next
            prev = curr
            curr = prev.next
        while dummy.next:
            print(dummy.next.val)
            dummy = dummy.next
        return dummy.next


if __name__ == "__main__":
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = None
    s = Solution()
    print(s.reverseKGroup(h1, 2))

