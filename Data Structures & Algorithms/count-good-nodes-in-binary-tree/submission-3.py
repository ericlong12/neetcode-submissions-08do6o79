# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def dfs(node, maxValue):

            if not node:
                return 0
            
            if node.val >= maxValue:
                goodCounter = 1
                maxValue = max(maxValue, node.val)
            
            else:
                goodCounter = 0

            
            
            goodCounter += dfs(node.left, maxValue)
            goodCounter += dfs(node.right, maxValue)
            return goodCounter

        return dfs(root, root.val)

        















        