# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        A = []
        B = []
        C = []
        while curr is not None:
            A.append(curr.val)
            curr = curr.next
        curr = l2
        while curr is not None:
            B.append(curr.val)
            curr = curr.next
        A = list(reversed(A))
        B = list(reversed(B))
        a = "".join(str(i) for i in A)
        b = "".join(str(i) for i in B)
        val = int(a) + int(b)
        val = list(str(val))
        val = list(reversed(val))
        val = list((int(i) for i in val))

        c = 0
        h = ListNode(val[c])
        curr = h
        while curr is not None:
            if c >= len(val) - 1:
                break
            c+=1
            curr.next = ListNode(val[c])
            curr = curr.next
        
        return h
