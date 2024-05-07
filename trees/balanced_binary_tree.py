# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # sub-function to find if balanced & height
        def dfs(root): # return bool, height of tree
            if not root:
                return (True, 0)
            left_balanced, left_h = dfs(root.left)
            right_balanced, right_h = dfs(root.right)
            current_balanced = (left_balanced and right_balanced and 
                            abs(left_h - right_h) <= 1)
            if not current_balanced:
                return (False, 0)
            return (True, 1 + max(left_h, right_h))
        return dfs(root)[0]

