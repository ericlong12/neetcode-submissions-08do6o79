class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for number in numSet:
            if number - 1 not in numSet:
                # this means it is a start
                length = 1
                while number + length in numSet:
                    # this means we get our current number add 1
                    length += 1
                longest = max(length, longest)
        return longest