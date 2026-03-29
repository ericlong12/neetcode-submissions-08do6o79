from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = deque()

        # we should add the root to the queue

        q.append(root)

        while q:
            lengthOfQ = len(q)
            level = []

            for index in range(lengthOfQ):
                currentNode = q.popleft()

                if currentNode:
                    level.append(currentNode.val)
                    q.append(currentNode.left)
                    q.append(currentNode.right)
                
            if level:
                answer.append(level)

        return answer

        