from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        answer = []

        queue.append(root) # this is to start the BFS

        while queue:
            level = []
            for index in range(len(queue)):
                node = queue.popleft()

                if node:
                    level.append(node.val)

                    queue.append(node.left)
                    queue.append(node.right)
                # after appending the node. 
            if level:
                answer.append(level)

        return answer












