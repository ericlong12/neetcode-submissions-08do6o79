class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        niggaSet = set(nums)

        lengthOfNiggaSet = len(niggaSet)
        lengthOfReg = len(nums)

        if lengthOfNiggaSet == lengthOfReg:
            return False
        

        return True