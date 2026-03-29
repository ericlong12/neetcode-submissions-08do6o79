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
        # we will create a deep copy.
        # first we look at the class Node, we see it needs an integer

        current = head
        # we can use a hashmap to connect it to the orginal

        # hashCopy
        hashCopy = {None:None}

        while current:
            copyNode = Node(current.val)
            hashCopy[current] = copyNode
            current = current.next
        # after this is running we have the base nodes. 
        # now we should align the random pointers



        # okay we did the first pass and got the needed info
        # now we should do the 2nd pass and insert the data

        
        current = head
        while current:
            copy = hashCopy[current]
            copy.next = hashCopy[current.next]
            copy.random = hashCopy[current.random]
            current = current.next

        return hashCopy[head]



