# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we return either true or false

        hasSeen = set()

        current = head

        while current:
            if current in hasSeen:
                return True
            
            else:
                hasSeen.add(current)
                current = current.next
        return False
