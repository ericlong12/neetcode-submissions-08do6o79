# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # to invert binary tree we swap only the childs
        if not root:
            return 

        def dfs(node):
            if not node:
                return

            bucket = node.left
            node.left = node.right
            node.right = bucket

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
        