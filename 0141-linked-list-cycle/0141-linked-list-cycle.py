# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        V = []

        while curr != None:
            if (curr in V):
                return True
            
            V.append(curr)
            curr = curr.next
        
        return False