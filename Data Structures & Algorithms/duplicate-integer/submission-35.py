class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        sizeSet = set(nums)
        # input nums = [1, 2, 3, 3]
        # sizeSet = (1, 2, 3)

        lengthOfSizeSet = len(sizeSet)
        # will return 3

        if lengthOfSizeSet == len(nums):
            return False

        if lengthOfSizeSet < len(nums):
            return True
