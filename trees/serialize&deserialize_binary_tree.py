# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time: O(n), Space: O(n)
class Codec:
    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ','.join(res)
            
        
    def deserialize(self, data):
        vals = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
