# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            

            if node.val >= maxVal:
                maxVal = max(maxVal, node.val)
                myCounter = 1

            else:
                myCounter = 0

            leftCounter = dfs(node.left, maxVal)
            rightCounter = dfs(node.right, maxVal)

            return int(leftCounter + rightCounter + myCounter)

        return dfs(root, root.val)




















        