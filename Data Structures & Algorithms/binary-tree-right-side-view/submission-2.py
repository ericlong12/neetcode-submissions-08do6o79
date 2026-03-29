from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can run a BFS and return the right most element at every level
        if not root:
            return []

        # set up a q
        q = deque()

        q.append(root)
        level = []

        while q:
            lengthOfQ = len(q)
            for index in range(lengthOfQ):
                node = q.popleft()
                if index == lengthOfQ - 1:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level
                









