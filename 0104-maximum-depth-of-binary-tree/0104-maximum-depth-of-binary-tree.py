# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def DFS(root, depth):
            nonlocal max_depth
            if not root:
                max_depth = max(max_depth, depth)
                return
            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)
        
        DFS(root, 0)
        return max_depth