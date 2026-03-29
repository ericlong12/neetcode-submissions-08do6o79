class Solution:
    def findMin(self, nums: List[int]) -> int:
        # compare left and right pointer
        # if leftPointer is greater than right pointer
        # [3,4,5,6,7,8,9,0,1,2]

        leftPointer = 0
        rightPointer = len(nums) - 1

        # we check if it is even rotated.
        # nums=[4,5,6,7]


        # new test case
        # nums=[4,5,6,7,0,1,2]


        # new test case
        # nums=[5,1,2,3,4]
        # left = 0 
        # right = 4
        # middle = 2
        while leftPointer < rightPointer:

            middlePointer = (leftPointer + rightPointer) // 2

            if nums[middlePointer] < nums[rightPointer]:
               rightPointer = middlePointer
               
            
            elif nums[middlePointer] > nums[rightPointer]:
                leftPointer = middlePointer + 1
                
        return nums[leftPointer]
            


