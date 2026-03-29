# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # in preorder. the node will always be first.
        # in in order. the node we give will partition the array left and right

        # we are given both preorder and inorder array

        # if there isn't anything to work with return none
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0]) #.index make it so that we return the index for the number we searching for
        root.left = self.buildTree(preorder[1 : middle + 1], inorder[:middle])
        root.right = self.buildTree(preorder[middle + 1: ], inorder[middle + 1 : ])
        return root



