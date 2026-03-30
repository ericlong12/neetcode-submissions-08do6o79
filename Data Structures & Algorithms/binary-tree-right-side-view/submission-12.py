from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        
        q = deque()
        q.append(root)

        if not root:
            return []

        answer = []
        while q:
            length = len(q)
            for index in range(len(q)):
                node = q.popleft()
   
                if index == length - 1:
                    answer.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        return answer










