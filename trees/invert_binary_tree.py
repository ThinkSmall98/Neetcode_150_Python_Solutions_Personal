# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # recursive
    # Time: O(n) where n = # of nodes in tree
    # Space: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if node is empty
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
    
    # iterative (BFS)
    # Time: O(n)
    # Space: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None

        queue = deque([root])
        while queue:
            # get current node
            current = queue.popleft()
            # swap left & right nodes
            current.left, current.right = current.right, current.left
            # check left & right nodes under current node & append to queue if exists
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

