# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # okay lets solve this problem using DFS

        def dfs(root) -> list:
            # we should get the base case if they are both null
            # we will return if it is balenced and the height
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balenced = (left[0] and right[0]) and (abs(left[1] - right[1]) <=1)

            # we need to get the height of the current subtree
            return [balenced, 1 + max(left[1], right[1])]
            
        return dfs(root)[0]
