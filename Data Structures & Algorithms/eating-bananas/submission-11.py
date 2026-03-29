class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours we have to eat all food
        # we have to eat all of the food in piles
        # piles[i] is the amount of food in that pile
        # the piles don't carry over,
        # if pile[i] = 2 
        # my eating speed is 10 -> then it takes 1 hours to finish that pile
        # if my eating speed is 2 - > then it would still take 1 hour to finsh
        # If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.


        # get the biggest pile.
        # we know that the eating speed is less than or equal to the max pile

        topEatingSpeed = max(piles)
        slowestEatingSpeed = 1
        slowestEatingSpeedValid = float('inf')
        # have a condition where our current speed MUST be fast or equal then h


        # runs the loop for 1 - maxpile
        # we can compute the middle
        while slowestEatingSpeed <= topEatingSpeed:
            currentEatingSpeed = (slowestEatingSpeed + topEatingSpeed) // 2
            hourCounter = 0
            for pile in piles:
                hourCounter += (pile + currentEatingSpeed - 1) // currentEatingSpeed
                # after doing this, we can see how long it took for us to finish
                # all the food
            if hourCounter <= h: # we ate too fast, can we do better?
                slowestEatingSpeedValid = min(slowestEatingSpeedValid, currentEatingSpeed)
                topEatingSpeed = currentEatingSpeed - 1
            
            elif hourCounter > h: # we ate too slow, not valid
                slowestEatingSpeed = currentEatingSpeed + 1
        return slowestEatingSpeedValid
            










