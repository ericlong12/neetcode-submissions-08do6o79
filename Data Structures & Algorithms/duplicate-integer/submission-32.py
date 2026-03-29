class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we return either true or false.
        # we return true of there is a duplicate. 

        # orginally, we want to use the brute force. 
        # our first pointer will be on threst index. 
        # will use 2 for loops

        # but we can do better using a set

        hasSeen = set(nums)

        if len(hasSeen) < len(nums):
            return True
        
        return False
