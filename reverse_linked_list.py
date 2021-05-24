"""
翻转链表
"""


def reverse_linked_list(head):
    if not head or not head.next:
        return head
    
    next = head.next
    head.next = None
    new_head = reverse_linked_list(next)
    next.next=head
    return new_head


def iter_reverse_linked_list(head):
    # 头插法
    if not head or not head.next:
        return head
    while(head):
        next = head.next
        head.next = new_list.next
        new_list.next = head
        head = next
    return new_list.next
    
