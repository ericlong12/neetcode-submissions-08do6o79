# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tom = head
        jerry = head

        while jerry and jerry.next:
            tom = tom.next
            jerry = jerry.next.next

            if tom == jerry:
                return True



        return False