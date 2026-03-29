# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we should check for p and q

        current = root
        biggerVal = max(p.val,q.val)
        smallerVal = min(p.val, q.val)

        while current:
            if current.val < p.val and current.val < q.val:
                current = current.right
            
            elif current.val > p.val and current.val > q.val:
                current = current.left
            
            elif current.val == p.val or current.val == q.val or (current.val < biggerVal and current.val > smallerVal):
                return current
        