# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def dfs(node, maxValue):
            answer = 0
            if not node:
                return 0
            
            if node.val >= maxValue:
                maxValue = max(maxValue, node.val)
                answer = 1
            else:
                answer =  0
            
            answer += dfs(node.left, maxValue)
            answer += dfs(node.right, maxValue)

            return answer
  
        return dfs(root, root.val)

            
            

















