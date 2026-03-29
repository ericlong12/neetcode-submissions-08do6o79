from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        queue = deque()
        queue.append(root)

        answer = []

        while queue:
            lenQ = len(queue)
            level = []

            for index in range(lenQ):
                node = queue.popleft()

                if node:
                    level.append(node)
                    # now we want to add its left and right children into the queue
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                answer.append(level[-1].val)

        return answer















