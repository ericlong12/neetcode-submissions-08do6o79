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
        # we will solve this problem by creating a dictionary
        # this dictionary will be to reference the nodes we have coppied.
        
        oldToNew = {None:None}
        
        current = head
        
        while current:
            copy = Node(current.val) # this will create a copy of every noded in the LL
            oldToNew[current] = copy # this will map the old node to the new Copy
            current = current.next # we go to the next node til null
        
        # we move our pointer to the start of the linked list now
        
        current = head
        
        while current:
            copy = oldToNew[current] # we reference the current new node.
            copy.next = oldToNew[current.next]
            copy.random = oldToNew[current.random]
            current = current.next
        
        # we return the head of the copied linked list

        return oldToNew[head]
            
        
        
        
        
        
        
        
        
        
        
