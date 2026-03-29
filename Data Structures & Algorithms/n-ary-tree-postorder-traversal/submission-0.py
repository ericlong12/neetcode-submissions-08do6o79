"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# we see there isn't left or right, there is just children
# children is a list of nodes

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        
        answer = []

        def dfs(root):
            if not root:
                return

            for child in root.children:
                dfs(child)
            answer.append(root.val)

        dfs(root)
        return answer





