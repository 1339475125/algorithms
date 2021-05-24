"""
合并两个排序的链表
"""

def merge_linked_list(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        head1.next = merge_linked_list(head1.next, head2)
        return head1
    else:
        head2.next = merge_linked_list(head1, head2.next)
        return head2