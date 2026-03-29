class Solution:
    def trap(self, height: List[int]) -> int:
        # get the max left at current element
        # get the max right at current element
        totalWeight = 0
        for currentIndex in range(len(height)):
            maxLeft = max(height[:currentIndex]) if currentIndex > 0 else 0
            maxRight = max(height[currentIndex+1:]) if currentIndex < len(height)-1 else 0
            minHeight = min(maxLeft,maxRight)

            # now we apply the formula
            currentWeight = minHeight - height[currentIndex]

            if currentWeight > 0:
                totalWeight += currentWeight

        return totalWeight
        
        