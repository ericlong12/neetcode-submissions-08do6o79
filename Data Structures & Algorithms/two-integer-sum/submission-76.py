class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force

        for indexI in range(len(nums)):
            for indexJ in range(len(nums)):
                if nums[indexI] + nums[indexJ] == target and indexJ != indexI:
                    return [indexI, indexJ]