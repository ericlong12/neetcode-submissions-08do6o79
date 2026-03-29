class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = set()

        # hasSeen (1, 2, 3)
        for number in nums:
            if number in hasSeen:
                return True
            if number not in hasSeen:
                hasSeen.add(number)
        
        return False

        

