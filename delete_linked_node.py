# -*- coding:utf-8 -*-
"""
在O(1)时间内删除链表节点
"""

class ListNode(object):

    def __int__(self, x):
        self.value = x
        self.next = None

    def __del__(self):
        self.value = None
        self.next = None

class Solution(object):

    def delete_node(self, head, del_node):
        if not head or not del_node:
            return None
        
        if del_node.next != None:
            del_node.value = del_node.next.value
            del_node.next = del_node.next.next
            del_node.next.__del__()
        elif del_node == head:
            head.__del__()
        else:
            node = head
            while node!=del_node:
                node = node.next
            node.next = None
            del_node.__del__()