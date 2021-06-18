# 分治法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge_two_lists(lists[0], lists[1])

        mid = len(lists) // 2
        list1 = lists[:mid]
        list2 = lists[mid:]
        return self.merge_two_lists(self.mergeKLists(list1), self.mergeKLists(list2))


    def merge_two_lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if(list1.val <= list2.val):
            head = list1
            head.next = self.merge_two_lists(list1.next, list2)
        else:
            head = list2
            head.next = self.merge_two_lists(list1, list2.next)
        return head
