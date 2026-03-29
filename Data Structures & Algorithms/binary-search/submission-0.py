from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middleIndex = (left + right) // 2
            middle = nums[middleIndex]

            if middle == target:
                return middleIndex
            elif middle < target:
                left = middleIndex + 1
            else:
                right = middleIndex - 1

        return -1
