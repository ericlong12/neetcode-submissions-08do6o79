class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # open with creating a dictionary
        my_dictionary = {}
        # now we enumerate through the list. create index and num
        for index, num in enumerate(nums):
            # create a complement, the number we are looking for;
            complement = target - num

            # add to the dictionary if the complement is in the dictionary
            if complement in my_dictionary:
                return [my_dictionary[complement], index]
            my_dictionary[num] = index