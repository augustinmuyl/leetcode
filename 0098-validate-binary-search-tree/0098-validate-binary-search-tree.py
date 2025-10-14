# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, float("inf"), float("-inf")]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left[0] and right[0] and left[2] < root.val < right[1]:
                return [True, min(left[1], root.val), max(right[2], root.val)]
            
            return [False, None, None]

        return dfs(root)[0]