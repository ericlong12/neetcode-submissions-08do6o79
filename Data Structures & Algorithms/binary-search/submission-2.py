class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the array is already sorted. we can implement a regular binary search. The point of this is to practice in python and then in java


        leftPointer = 0
        rightPointer = len(nums) - 1
        # we should return the index

        while leftPointer <= rightPointer:
            #while the condition is true we try to find the middle

            middle = (leftPointer + rightPointer) // 2
            # we use floor division here to remove the decimal pointer

            # now we actually make the needed checks
            if target == nums[middle]:
                return middle

            elif target > nums[middle]:
                # we should make the number bigger to match the target
                leftPointer = middle + 1

            else:
                rightPointer = middle - 1
            
        # if no match then return -1
        return -1