# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can do in order traversal and subtract from k until it reaches 0
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
                # this runs until we reach the very end

            current = stack.pop()

            k -= 1
            if k == 0:
                return current.val
            
            current = current.right


