# -*- coding:utf-8 -*-
"""
删除链表中重复的结点
"""


def delete_dup_data(head):
    if not head or not head.next:
        return head
    
    lnext = head.next
    if head.value == lnext.val:
        while(lnext!=None and head.val == lnext.val):
            lnext = lnext.next
            return delete_dup_data(lnext)
    else:
        head.next = delete_dup_data(head.next)
        return head
j

