class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers one at the start one at the end
        leftPointer = 0
        rightPointer = len(numbers) - 1 
        while leftPointer < rightPointer:
            if numbers[leftPointer] + numbers[rightPointer] == target:
                return [leftPointer +1, rightPointer+1]
            elif numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer -= 1
            else:
                leftPointer +=1

            
        