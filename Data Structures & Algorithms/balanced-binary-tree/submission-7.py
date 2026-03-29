# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # have something to hold height
        # have something to hold true
        # keep on calling it as long as true

        def dfs(node):
            if not node:
                # if the node is not there return 0
                # this means that there is no children
                return [True, 0]

            left = dfs(node.left) # we go deep all to the left
            right = dfs(node.right) # we go deep all the way to the right

            balenced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # checks if both are true and not greater than 1
            # we make 3 boolean values

            return [balenced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
















