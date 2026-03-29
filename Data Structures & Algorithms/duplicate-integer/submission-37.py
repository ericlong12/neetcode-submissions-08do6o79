class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index in range(len(nums)):
            for index2 in range(index + 1,len(nums)):
                if nums[index] == nums[index2]:
                    return True
        
        return False
