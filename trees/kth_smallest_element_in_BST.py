# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive (DFS)
    # Time: O(n)
    # Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []
        return inOrder(root)[k - 1]

    # Iterative (BFS)
    # Time: O(n + k)
    # Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
