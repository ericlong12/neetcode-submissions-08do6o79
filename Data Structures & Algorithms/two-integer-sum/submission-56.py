class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary
        map = {}
        for index, num in enumerate(nums):
            complement = target - nums[index]
            if complement in map:
                return [map[complement], index]
            map[num] = index
            