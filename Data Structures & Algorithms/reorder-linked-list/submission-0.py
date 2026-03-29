# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # saves the start of the 2nd LL
        secondPartOfLL = slow.next

        # cuts the LL into two parts
        slow.next = None

        # now we should reverse the 2nd part

        current = secondPartOfLL
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        # now previous is reversed

        firstHalf = head
        secondHalf = previous

        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = temp1

            firstHalf = temp1
            secondHalf = temp2



        