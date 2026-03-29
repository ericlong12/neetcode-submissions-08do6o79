# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointers
        # slow pointer, moves once per iteration
        # fast pointer, moves twice per iteration

        # IF those two pointer are ever at the same node. 
        # we know that there MUST be a cycle

        # if the fast pointer reaches null, we know there is no cycle
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next: # if this can't run. we exit?
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True


        return False
            
        












