# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
 

        # 1 -> 2 -> 3 -> None


        # None <- 1 <- 2 <- 3


    # None [previous]
         #1 currently holds the current
         # bucket. right now hold the 2
       # 1 -> 2 -> 3 -> None
        current = head
        previous = None



        while current:
            # holds the 2
            bucket = current.next

            # this makes 1 -> None
            current.next = previous

            # now we make previous equal to 1, instead of None
            previous = current

            # Now we say that our current pointer is at 2, and previous at 1
            current = bucket
        
        return previous











