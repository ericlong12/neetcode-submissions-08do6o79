class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # we start by soring the array nums

        nums.sort()
        # Input: nums = [-1,0,1,2,-1,-4]

       #                        I.            L  R 
        # sortedInput: nums = [-4, -1, -1, 0, 1, 2]
        # lets go run index:
        answer = []

        for index in range(len(nums)):
            leftPointer = index + 1
            rightPointer = len(nums) - 1

        

            if nums[index] > 0:
                break
                # we exit the loop, bc we know that all the number to the right
                # of index MUST be either equal or larger than nums[index]

            if index > 0 and nums[index - 1] == nums[index]:
                continue

            if nums[index] <= 0:
                while leftPointer < rightPointer:
                    if nums[index] + nums[leftPointer] + nums[rightPointer] == 0:
                        answer.append([nums[index], nums[leftPointer], nums[rightPointer]])
                        leftPointer += 1
                        rightPointer -= 1

                        while leftPointer < rightPointer and nums[leftPointer - 1] == nums[leftPointer]:
                            leftPointer += 1
                    
                    elif nums[index] + nums[leftPointer] + nums[rightPointer] < 0:
                        leftPointer += 1
                        
                    elif nums[index] + nums[leftPointer] + nums[rightPointer] > 0:
                        rightPointer -= 1
        return answer










            

