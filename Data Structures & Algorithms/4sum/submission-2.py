class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # okay so we have to add 4 numbers to add up to the target

        # we can do this by sorting and two pointers


        nums.sort()


        # two fixed numbers then use two pointers

        # to get two fixed numbers we need two for loops
        answer = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue

            for index2 in range(index + 1, len(nums)):
                if index2 > index + 1 and nums[index2] == nums[index2 -1]:
                    continue
                # okay now we can do two pointers

                leftPointer = index2 + 1
                rightPointer = len(nums) - 1


                while leftPointer < rightPointer:
                    total = nums[index] + nums[index2] + nums[leftPointer] + nums[rightPointer]
                    if total == target: 
                        
                        answer.append([nums[index], nums[index2], nums[leftPointer],nums[rightPointer]])
                        rightPointer -= 1
                        leftPointer += 1

                        while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                            leftPointer += 1
                        
                        while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                            rightPointer -= 1

                    elif total > target:
                        rightPointer -= 1
                    elif total < target:
                        leftPointer += 1
        return answer


                
            

