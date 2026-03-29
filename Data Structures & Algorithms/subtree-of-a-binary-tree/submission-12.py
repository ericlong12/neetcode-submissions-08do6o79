# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def isSameTree(root, subRoot): #will return a boolean
            # should only compare same tree
            if not root and not subRoot:
                return True

            if root and not subRoot:
                return False
            
            if not root and subRoot:
                return False
            
            if root.val != subRoot.val:
                return False

            return isSameTree(root.right, subRoot.right) and isSameTree(root.left, subRoot.left)
            
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSameTree(root,subRoot): # i never thought of using it like that. 
        #this why when isSameTree returns false. then we can still run the algorithm
            return True
        
        #this case we want to go to the compare subRoot with the left and right subtrees of Root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        
        



