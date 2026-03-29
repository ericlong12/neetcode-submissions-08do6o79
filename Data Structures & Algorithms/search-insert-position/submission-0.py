class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # we will return the index of our target value
        # if that value cannot be found, we return the index
        # where it should be found

        # we can start with a left pointer
        # right pointer

        leftPointer = 0
        rightPointer = len(nums) - 1

        # while left pointer is equal to right, 
        while leftPointer <= rightPointer:
            middle = (leftPointer + rightPointer) // 2
            # we use floor division

            if nums[middle] == target:
                return middle
            
            elif nums[middle] < target:
                leftPointer = middle + 1
            
            elif nums[middle] > target:
                rightPointer = middle - 1
        return leftPointer