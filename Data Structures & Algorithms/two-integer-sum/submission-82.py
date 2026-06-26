class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we have to add up two numbers to reach the target


        # we return the index of the numbers being used

        seen = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in seen:
                # then we just return the answer
                return[seen[complement],index]
            
            # if its not there then we add it
            seen[nums[index]] = index

