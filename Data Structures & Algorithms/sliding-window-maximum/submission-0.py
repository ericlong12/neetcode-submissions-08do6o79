class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        lengthOfArray = len(nums)
        numOfSlides = lengthOfArray - k + 1

        for index in range(numOfSlides):
            windowMax = max(nums[index : index + k])
            ans.append(windowMax)

        return ans
