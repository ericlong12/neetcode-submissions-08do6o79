class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # the index will be the node of a linked list
        # the nums[index] will be the pointer of the linked list

        # we can do a cycle detection with slow and fast pointer

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        
        # CYCLE DETECTED!!!
        # we actually want to find the start of the cycle

        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return fast
        
        









