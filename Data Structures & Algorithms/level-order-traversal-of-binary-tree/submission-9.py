from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for this problem we should return each level an put inside a list

        # this looks like a BFS

        queue = deque()

        queue.append(root)
        answer = []

        while queue:
            lengthOfQ = len(queue)
            level = []

            for index in range(lengthOfQ):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    level.append(node.val)
            if level:
                answer.append(level)

        return answer

            
















        