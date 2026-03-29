class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we know that we can only sell at a later price

        # we want to buy at the lowest price and sell high

        leftPointer = 0

        maxProfit = 0

        for index in range(len(prices)):
            # we want to buy at a small number
            if prices[index] < prices[leftPointer]:
                leftPointer = index # we are doing this to buy at lower price

            elif prices[index] > prices[leftPointer]:
                maxProfit = max(maxProfit, prices[index] - prices[leftPointer])
            
        return maxProfit

