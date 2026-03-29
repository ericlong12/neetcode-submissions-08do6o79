class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix 
        # Input: nums = [1,2,4,6]
        # [1, 1, 2, 8]

        answer = [1] * len(nums)

        # fill in values for prefix
        prefix = 1

        for index in range(len(nums)):
            answer[index] = prefix
            prefix *= nums[index]

        # now we will do it in place and solve for post
        postfix = 1

        for index in range(len(nums) - 1, -1, -1):
            answer[index] *= postfix
            postfix *= nums[index]
        
        return answer

