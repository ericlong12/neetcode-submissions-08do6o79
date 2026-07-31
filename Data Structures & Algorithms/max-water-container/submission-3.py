class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1

        maxAnswer = 0

        while leftPointer <= rightPointer:
            distance = rightPointer - leftPointer
            height = min(heights[rightPointer], heights[leftPointer])
            maxAnswer = max(maxAnswer, distance * height)
            if heights[leftPointer] >= heights[rightPointer]:
                rightPointer -= 1

            else:
                leftPointer += 1
            
        return maxAnswer
