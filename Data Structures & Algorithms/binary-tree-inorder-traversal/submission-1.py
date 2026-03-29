# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # in order traversal

        # leftnode -> RootNode - > rightNode

        if not root:
            return []
        
        answer = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            answer.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return answer










