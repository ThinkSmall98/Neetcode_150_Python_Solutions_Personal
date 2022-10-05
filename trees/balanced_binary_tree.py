# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n), Space: O(n)
    def isBalancedHelper(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True, -1
        # check subtrees to see if they're balanced
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, leftHeight
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, rightHeight
        # if substrees balanced, check if current tree is balanced using height
        return (abs(leftHeight - rightHeight) <= 1), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]
        
# Bottom-up recursion
'''
bottom-up approach is a reverse of the logic of the top-down approach since we first check if the child subtrees are balanced before comparing their heights
