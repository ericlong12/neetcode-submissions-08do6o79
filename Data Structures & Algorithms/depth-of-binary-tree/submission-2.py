# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we have to find the height/depth of the tree
        self.height = 0

        def dfs(root) -> int:
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            self.height = 1 + max(leftHeight,rightHeight)

            return 1 + max(leftHeight,rightHeight)
        dfs(root)
        return self.height
            













