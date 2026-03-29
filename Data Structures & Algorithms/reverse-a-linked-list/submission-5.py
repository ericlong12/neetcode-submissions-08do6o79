# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
      #  1 -> 2 -> 3 -> null # this is what is given to us
     #   null <- 1 <- 2 <- 3 # this is what we wanna return




        if not head:
            return None

        current = head
        previous = None


        while current:
            # 1 -> 2
            bucket = current.next

            # None <- 1
            current.next = previous
            
            # now none pointer moves to the one
            previous = current
            current = bucket

        return previous



            














