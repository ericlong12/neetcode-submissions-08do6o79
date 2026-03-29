# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val # current node
#         self.left = left # left child
#         self.right = right # right child

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # we have to return the root node again
        # we are swapping the nodes in place

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
        