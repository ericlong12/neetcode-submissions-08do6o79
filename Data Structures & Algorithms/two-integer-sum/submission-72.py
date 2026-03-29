class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we add up two number to see if it reaches the target
        # this is brute force

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]