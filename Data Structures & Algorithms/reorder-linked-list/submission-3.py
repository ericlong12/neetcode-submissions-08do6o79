# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # we need to find the middle of the linkedList
        curr = head
        slow = curr
        fast = curr.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now we know that fast is at the end of LL
        # we know that slow is at the halfway point


        # first we need to reverse linkedList
        previous = None
        current = slow.next
        slow.next = None

        while current:
            bucket = current.next
            current.next = previous
            previous = current
            current = bucket

        # now we combine
        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            



            
            