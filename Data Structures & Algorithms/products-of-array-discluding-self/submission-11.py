class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we will be solving by using post and prefix.
        # lets make an answer sheet
        lengthOfNums = len(nums)
        answer = [1] * lengthOfNums

        # postfix
        postfix = 1
        for index in range(lengthOfNums):
            answer[index] *= postfix
            postfix *= nums[index]

        # prefix
        prefix = 1
        for index in range(lengthOfNums - 1, -1, -1):
            answer[index] *= prefix
            prefix *= nums[index]
        return answer


