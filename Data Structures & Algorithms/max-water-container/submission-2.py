class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0

        # get the difference between our two pointer
        # min height of both our pointer.

        # compute the max
        # they want us to return the max value of water we can hold

        # two pointers
        # one starts at the beginning

        leftPointer = 0


        # another one will start at the end
        rightPointer = len(heights) - 1


        # we can compare the heights of the two pointers
        # we move the pointer with the lower height.

        # we do this until left == right
        # while left < right

        while leftPointer < rightPointer:
            distance = rightPointer - leftPointer 
            currentWater = distance * min(heights[leftPointer],heights[rightPointer])
            maxWater = max(maxWater, currentWater)
            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        
        return maxWater
            







