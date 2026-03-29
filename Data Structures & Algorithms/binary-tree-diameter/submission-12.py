# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we need a global variable, which is our answer (diameter)
        self.result = 0

        def dfs(current) -> int: #returns the height
            if not current:
                return 0

            leftHeight = dfs(current.left)
            rightHeight = dfs(current.right)

            self.result = max(self.result, leftHeight + rightHeight)

            return 1 + max(leftHeight,rightHeight)

        dfs(root)
        return self.result






