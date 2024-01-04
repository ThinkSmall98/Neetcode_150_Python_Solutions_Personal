# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS (Recursive)
    # Time: O(n)
    # Space: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_len = 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    # BFS (Iteration + stack)
    # Time: O(n)
    # Space: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        max_depth = 0
        while stack:
            curr_depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, curr_depth)
                stack.append((curr_depth + 1, node.left))
                stack.append((curr_depth + 1, node.right))
        return max_depth

