from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theSet = set()
        for i in range(len(nums)):
            if nums[i] in theSet:
                return True
            else:
                theSet.add(nums[i])
            
        return False


        
            
        
        

         