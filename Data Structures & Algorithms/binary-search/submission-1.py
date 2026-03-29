class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [2, 4, 8]

        #find if the target number is inside of nums.
        # if it is, we return the index.
        # otherwise we should return -1


        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer: # 7/2 - > 3
            middle = (leftPointer + rightPointer) // 2
            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                rightPointer = middle - 1

            elif nums[middle] < target:
                leftPointer = middle + 1

        return -1
            

            



