class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # lets solve using a hashMap

        # we want to return the index.

        # we will use complment:index

        complements = {}

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in complements:
                return [complements[complement], index]

            elif complement not in complements:
                complements[nums[index]] = index
