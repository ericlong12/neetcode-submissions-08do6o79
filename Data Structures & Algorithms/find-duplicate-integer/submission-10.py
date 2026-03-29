class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can have one where 
        
        # we will have one fast pointer 
        # we will have one slow pointer
        # this will be a cycle detection algorithm


        fastPointer = 0
        slowPointer = 0

        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                break
        
        # okay we found a cycle. now we want to find the start of the cycle
        slowPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]
            if slowPointer == fastPointer:
                return slowPointer

        

