"""
1->2->3->4->5
1->3->5->2->4
"""

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def link_sort(head):
    if not head or not head.next:
        return head
    ji_node = head
    ou_node = head.next
    end_node = ou_node
    while(ji_node.next and end_node.next):
        ji_node.next = end_node.next
        ji_node = ji_node.next
        end_node.next = ji_node.next
        end_node = end_node.next
    ji_node.next=ou_node
    return head


link1 = ListNode(1)
link2 = ListNode(2)
link3 = ListNode(3)
link4 = ListNode(4)
link5 = ListNode(5)

link1.next = link2
link2.next = link3
link3.next = link4
link4.next = link5
print(link1)
print(link_sort(link1))
