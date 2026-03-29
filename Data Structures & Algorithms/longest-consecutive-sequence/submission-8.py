class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the method is to use a set.
        # check if there is the element in the set
        # do this by seeing if there is a smaller num in the set
        # make a length and make a longest
        length = 0
        longest = 0 
        
        mySet = set(nums)
        for num in mySet:
            if num-1 in mySet:
                length = 1
                continue
            # we add a num + length num is the current number
            # length is the length of our consecutive sequence
            while num + length in mySet:
                length +=1
                longest = max(longest, length)
        return longest