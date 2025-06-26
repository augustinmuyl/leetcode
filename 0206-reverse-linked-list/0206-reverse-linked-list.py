# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        curr = head
        A = []
        while curr is not None:
            A.append(curr.val)
            curr = curr.next
        A = list(reversed(A))
        h = ListNode()
        curr = h
        for i, v in enumerate(A):
            curr.val = v
            if i == len(A)-1:
                curr.next = None
            else:
                curr.next = ListNode(A[i+1])
            curr = curr.next
        
        return h
