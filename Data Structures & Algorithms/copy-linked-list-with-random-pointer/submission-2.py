"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDictionary = {None:None}

        # new we go though the orginal list.
        # we map their nodes, 
        # key: the node itself
        # value: copy of the node

        current = head

        while current:
            copy = Node(current.val)
            copyDictionary[current] = copy
            current = current.next

        
        # after this we should have a dictionary of every node in the linked list

        current = head

        while current:
            copy = copyDictionary[current]
            copy.next = copyDictionary[current.next]
            copy.random = copyDictionary[current.random]
            current = current.next
        return copyDictionary[head]

            








