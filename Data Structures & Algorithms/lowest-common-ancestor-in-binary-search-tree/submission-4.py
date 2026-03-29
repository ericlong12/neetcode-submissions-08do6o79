# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 5 = root
        if not root:
            return False
        # q = 4, p = 1 
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, q, p)

        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, q, p)
        
        else:
            return root
        

        
