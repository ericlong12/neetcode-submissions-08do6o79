# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post order is we do the childs before the parent. we do left then right


        result = []


        def postorder(root):
            if not root:
                return

            # we want to go to the far left
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result









