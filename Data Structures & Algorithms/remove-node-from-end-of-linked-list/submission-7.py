# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()

        dummyNode.next = head
        leftPointer = dummyNode
        rightPointer = head

        # we have to offset the right
        for index in range(n):
            rightPointer = rightPointer.next

            # now we have offset the rightPointer


        # we have to get left Pointer at the index right before
        # the node we want to delete


        while rightPointer:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

            # this stops when rightPointer = null,
            # Leftpointer is now at one node before the nth last

        leftPointer.next = leftPointer.next.next

        return dummyNode.next












