"""
链表中倒数第k个节点
双指针
"""


def find_k_to_tail(head, k):
    if not head:
        return None
    p1 = head
    while(p1):
        p1 = p1.next
        k = k -1
        if k <=0:
            break
    if(k > 0):
        return None
    p2 = head
    while (p1):
        p1 = p1.next
        p2 = p2.next
    return p2

