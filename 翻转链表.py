class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def ReverseList(pHead):
    # write code here
    if not pHead or not pHead.next:
        return pHead
    pre = None
    cur = pHead
    tmp = pHead
    while tmp.next:
        tmp = tmp.next
        cur.next = pre
        pre = cur
        cur = tmp
    cur.next = pre
    import pdb
    pdb.set_trace()
    return cur


link1 = ListNode(1)
link2 = ListNode(2)
link3 = ListNode(3)
link4 = ListNode(4)
link5 = ListNode(5)

link1.next = link2
link2.next = link3
link3.next = link4
link4.next = link5
print(ReverseList(link1))