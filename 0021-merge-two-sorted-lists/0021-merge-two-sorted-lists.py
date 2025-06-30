# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        h = ListNode()
        curr = h
        while list1 or list2:
            if list1 is None and list2 is None:
                return h
            if list1 is None:
                curr.val = list2.val
                list2 = list2.next
            elif list2 is None:
                curr.val = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            if list1 is None and list2 is None:
                return h
            curr.next = ListNode()
            curr = curr.next
        return h
        