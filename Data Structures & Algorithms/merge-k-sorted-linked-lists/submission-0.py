# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        overall_min = float('inf')
        overall_max = float('-inf')

        # Step 1: Determine overall_min and overall_max
        for node in lists:
            while node:
                if node.val < overall_min:
                    overall_min = node.val
                if node.val > overall_max:
                    overall_max = node.val
                node = node.next

        # Fix: Return None if no values were found
        if overall_min == float('inf') or overall_max == float('-inf'):
            return None
        
        # Step 2: Initialize frequency dictionary
        frequency_dict = {i: 0 for i in range(overall_min, overall_max + 1)}

        # Step 3: Populate frequency dictionary from all lists
        for node in lists:
            while node:
                if node.val in frequency_dict:
                    frequency_dict[node.val] += 1
                node = node.next

        # Step 4: Create new merged linked list from frequency dictionary
        dummy_head = ListNode(0)
        current = dummy_head

        for number, count in frequency_dict.items():
            for _ in range(count):
                current.next = ListNode(number)
                current = current.next

        return dummy_head.next
