class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary
        dic = {}

        # enumerate through the list to get index and loops through whole list
        for index, num in enumerate(nums):
            #create a complement
            complement = target - num

            # fill in the dictionary with new values. then check if the values in the dictionary is the number that you are looking for;
            if complement in dic:
                return [dic[complement],index]
            dic[num] = index
            