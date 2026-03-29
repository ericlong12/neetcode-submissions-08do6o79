class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want to return the index

        dictionary = {}

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in dictionary:
                return [dictionary[complement] , index]
            else:
                #key should be the complement, the value should be the index
                dictionary[nums[index]] = index
        

        