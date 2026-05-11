class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # this solution will be a backtracking.

        # we make the result to be returned

        result = []

        # we will use recursion on the main function

        # this is the base case. aka we are on the leaf node.
        # the idea is that we will be popping from the nuns list
        # then appending to get every order
        if len(nums) == 1:
            return [nums.copy()] # we do it like this because our answer will be a list of lists

        # we want to go through every value in nums:
        for index in range(len(nums)):
            # save the number you poped as n
            poppedNumber = nums.pop(0)

            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(poppedNumber)
            result.extend(permutations)
            nums.append(poppedNumber)

        return result
