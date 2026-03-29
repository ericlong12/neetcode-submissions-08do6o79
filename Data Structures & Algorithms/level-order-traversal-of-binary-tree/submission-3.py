from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\

        # get the base case
        if not root:
            return []

        # the answer will be a list of lists
        answer = []

        # we set up the queue
        q = deque()

        # now we should add the root node to the q
        q.append(root)

        # now the root is in the queue
        # we should pop the root and add its children

        # in order to do this we will do it in a clean way
        # lets run a while condition to run as long as q has elements in it

        while q:
            # we get the current length of q so that we know the levels
            lengthOfQ = len(q)
            whatsInTheLevel = []

            for index in range(lengthOfQ):
                node = q.popleft()
                # now that we just popped, and are holding onto
                # the node we are currently on (popped)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                whatsInTheLevel.append(node.val)
            
            answer.append(whatsInTheLevel)

        return answer
                
                







