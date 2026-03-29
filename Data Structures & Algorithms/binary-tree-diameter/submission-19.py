# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # we have a global variable
        self.maxAnswer = 0

        def dfs(node): 
            # compute at each node, its diameter
            # get total length of both left and right child
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxAnswer = max(self.maxAnswer, left + right)
            return 1 + max(left, right)

        
        dfs(root)
        return self.maxAnswer


