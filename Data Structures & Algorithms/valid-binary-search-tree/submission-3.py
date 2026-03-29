# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxVal = float("inf")
        minVal = float("-inf")

        # our current node has to be between left and right.
        # our left node has to be smaller than min Val
        # our right node has to be bigger than 

        def dfs(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, minVal, maxVal)
            









