class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary key: value
        # we have to add to check if its in target

        # subtracting from target to check if its in the dictionary

        # we can use key = index, value = number

        # we want both value and the index
        # therefore we can use enumerate

        # make dictionary
        complements = {}

        for index, number in enumerate(nums):
            # figure out what number we are looking for
            complement = target - number

            if complement in complements:
                return [complements[complement], index]
            
            if complement not in complements:
                complements[number] = index





