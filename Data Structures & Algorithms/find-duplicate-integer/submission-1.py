class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # you are given an array. 
        # solve this problem by using two pointers
        # increment the 2nd pointer when it doesn't match the first
        # increment the full length of the array

        lengthOfArray = len(nums)

        left = 0
        # pointer A should use the index
        right = lengthOfArray - 1



        # use a while loop and a bunch of if statements to solve this one
        while left < lengthOfArray:
            if nums[left] == nums[right] and right != left:
                return nums[left]
            
            if right == left:
                left += 1
                right = lengthOfArray - 1


            else:
                right -= 1


            



        