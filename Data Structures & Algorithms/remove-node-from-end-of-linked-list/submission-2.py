# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we have to remove the nth node
        # we have have two pointers
        
        dummy = ListNode()
        dummy.next = head

        leftPointer = dummy
        
        rightPointer = head

        for index in range(n):
            rightPointer = rightPointer.next
        

        while rightPointer:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
            # rightPointer is at null right now
        leftPointer.next = leftPointer.next.next

        return dummy.next

















        