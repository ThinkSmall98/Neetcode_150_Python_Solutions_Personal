# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row)
        return res

    # DFS
    # Time: O(n), Space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            # append current node value
            levels[level].append(node.val)
            # process  child nodes for next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)
        return levels
