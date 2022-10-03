# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Time: O(n), Space: O(n) - recursion stack
    def maxDepth(self, root):
        if not root:
            return 0
        left_h = self.maxDepth(root.left)
        right_h = self.maxDepth(root.right)
        return max(left_h, right_h) + 1
