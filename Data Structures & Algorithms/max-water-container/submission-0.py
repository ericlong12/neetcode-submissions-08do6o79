class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # solve this question by using 2 pointer

        # go through the list of integers
            left = 0
            right = len(heights) - 1

            result = 0

            #right is the width between those two pointers

            while left < right:
                width = right - left
                area = min(heights[left], heights[right]) * width
                result = max(area, result)

                if heights[left] >= heights[right]:
                    right -= 1

                elif heights[left] < heights[right]:
                    left += 1 


            return result
