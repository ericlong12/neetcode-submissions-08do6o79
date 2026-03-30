# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we have to return the lowest common ancestor
        # we know that the root is going to be an ancestor


        # the the root is between those two number it is an ancestor

        current = root


        while current:
            if current.val > p.val and current.val > q.val:
                # we want to switch to the left subtree
                current = current.left
            
            elif current.val < p.val and current.val < q.val:
                # we want to switch to the right subtree
                current = current.right
            
            else:
                return current
                # the last case is that the current number is either one
                # of the p or q, or that it is between those two numbers
            
            















