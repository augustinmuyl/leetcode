# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs return rightmost element per row

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        q = deque([root])
        rm = root
        res = [rm.val]

        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
            if q and node == rm:
                rm = q[-1]
                res.append(rm.val)
        
        return res