class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        leftPointer = 0
        rightPointer = len(nums) - 1
        
        # target = 4

        # L = 0. ->3
        # R = 5. -> 2

        # M = 2. ->6

        # because we know that our target is smaller than middle. 
        # we should search the part of the array which is larger

        # target = 3
        # nums=[3,5,1]

        #target is 4
        # Input: nums = [3,4,5,6,1,2]


        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2
            if nums[middlePointer] == target:
                return middlePointer

            elif nums[leftPointer] <= nums[middlePointer]: # this left half is sorted
                if nums[leftPointer] <= target < nums[middlePointer]:
                    rightPointer = middlePointer - 1
                else:
                    leftPointer = middlePointer + 1
            
            else:
                if nums[rightPointer] >= target > nums[middlePointer]:
                    leftPointer = middlePointer + 1
                
                else: 
                    rightPointer = middlePointer - 1


        return - 1
                    

                















