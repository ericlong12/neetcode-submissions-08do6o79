# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDiameter = 0



        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) #height of tree
            right = dfs(node.right) #height of tree

            # call + 1 every time to count depth
            self.maxDiameter = max(self.maxDiameter, left + right)

            return 1 + max(left,right) # actually counting height

        dfs(root)
        return self.maxDiameter











