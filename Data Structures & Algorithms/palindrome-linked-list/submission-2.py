# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # we have a linked list. if it reads the same  backwards as frontwards then it is true


        # we can implement a two pointer method but head is a ListNode


        #in that case if we are able to find the  middle of the linked list then work backwards from there

        # to find the middle we can do fast and slow pointers then reverse it

        # get the length of the linked list

        # we should just copy the orginal head then reverse it then compare


    

        if not head or not head.next:
            return True

        # we start both pointers at the same spot
        slow = head
        fast = head

        # now we should find the middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # okay now we have found the middle of the linked list

        # we should now reverse it from the show plointer because it is in the middle
        previous = None

        while slow:
            bucket = slow.next
            slow.next = previous
            previous = slow
            slow = bucket


        # now all we gotta do is compare the first and 2nd half

        left = head
        right = previous 

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True




        