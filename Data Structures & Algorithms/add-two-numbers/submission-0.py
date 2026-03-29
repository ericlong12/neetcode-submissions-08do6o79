# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def appendZeros(head: ListNode, n: int) -> ListNode:
            if not head:
                head = ListNode(0)
                n -= 1

            current = head
            while current.next:
                current = current.next

            for _ in range(n):
                current.next = ListNode(0)
                current = current.next

            return head

        def getLength(head: ListNode) -> int:
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        lengthOfl1 = getLength(l1)
        lengthOfl2 = getLength(l2)

        if lengthOfl1 > lengthOfl2:
            l2 = appendZeros(l2, lengthOfl1 - lengthOfl2)
        elif lengthOfl1 < lengthOfl2:
            l1 = appendZeros(l1, lengthOfl2 - lengthOfl1)

        remainder = 0
        head = l2  # Keep head of result list to return later

        while l1 and l2:
            total = l1.val + l2.val + remainder

            if total >= 10:
                remainder = 1
                l2.val = total - 10
            else:
                remainder = 0
                l2.val = total

            l1 = l1.next
            prev = l2
            l2 = l2.next

        # If there is a carry left after finishing both lists, append a new node
        if remainder == 1:
            prev.next = ListNode(1)

        return head
