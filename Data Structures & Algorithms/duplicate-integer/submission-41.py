class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # okay lets see contains duplicate
        # we can do this by using a set

        return not len(set(nums)) == len(nums)