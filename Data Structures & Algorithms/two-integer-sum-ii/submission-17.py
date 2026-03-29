class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have to note that we are actually doing 1 index

        # we will have 2 pointers.
        # left pointer will start at index 0 
        # right pointer will start at index len(numbers)


        leftPointer = 0
        rightPointer = len(numbers) - 1

        while leftPointer < rightPointer:
            if numbers[leftPointer] + numbers[rightPointer] == target:
                return [leftPointer + 1, rightPointer + 1]

            elif numbers[leftPointer] + numbers[rightPointer] < target:
                leftPointer += 1
            
            elif numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer -= 1
    
