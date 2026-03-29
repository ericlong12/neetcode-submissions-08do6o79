class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this one uses a hashmap

        mapHash = {} # complement:index

        for index, number in enumerate(nums):
            complement = target - number
            if complement in mapHash:
                return [mapHash[complement], index]
            else:
                mapHash[number] = index
            