"""
一个链表张包含环，找到这个环的入口节点
快慢指针
"""


def get_node_of_loop(phead):
    if not phead or not phead.next:
        return None
    slow = phead.next.next
    fast = phead.next
    while(slow != fast):
        slow = phead.next.next
        fast = phead.next
    fast = phead
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    return slow

