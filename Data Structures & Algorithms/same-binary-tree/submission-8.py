# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # dfs

        # check if current node is the same

        # check if left and right node are the same

        # recurse on this and if we finish. True

        # if we short circuit, false

        def dfs(tree1, tree2) -> bool:
            if not tree1 and not tree2:
                return True
            if not tree1:
                return False
            if not tree2:
                return False

            return tree1.val == tree2.val and dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)


        return dfs(p,q) # two trees












