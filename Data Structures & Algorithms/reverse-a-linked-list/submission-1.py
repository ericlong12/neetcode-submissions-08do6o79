# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None

        current = head

        while current:
            # save the value of the next pointer into temp
            # for the first run this is saving our way to node 2
            temp = current.next

            # then we have to set the current node's pointer to the previous
            current.next = previous 

            # now we have to move the cursor to the next node
            previous = current
            current = temp

        return previous

        
            
            