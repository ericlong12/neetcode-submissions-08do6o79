class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we want to find the start of a sub sequence.

        # sets are really for checking if something exists.

        numberSet = set(nums)
        maxLength = 0

        for number in nums:
          counter = 0
          if number - 1 not in numberSet:
            # we are IF a number is the start of a subsequence 

            # we know that our current number is in max length
            trackNumber = number
            while trackNumber in numberSet:
              counter += 1
              trackNumber += 1
              maxLength = max(counter, maxLength)

        return maxLength
            

