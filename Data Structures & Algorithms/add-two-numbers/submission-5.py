# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we create a dummy node, bc we are creating a new linked list
        # and returing that as the answer

        dummy = ListNode()
        current = dummy


        carry = 0

        while l1 or l2 or carry: # while there are still 2 linked lists:
            # now we add them

            # now we want to add the number in the one th space
            number1 = l1.val if l1 else 0
            number2 = l2.val if l2 else 0
            total = (number1 + number2 + carry)

            value = total % 10
            carry = total // 10 # this is the carry

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current.next = ListNode(value) # add this to our result
            current = current.next
        return dummy.next
















