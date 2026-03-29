class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Input: piles = [1,4,3,2], h = 9
        # Output: 2

        # we get to choose eating speed
        # our job is to find the slowest eating speed possible
        #which can allow us to eat all of the food in 9 hours

        # eating speed is 4 -> True because 4 <= 9 
        # 1, 1, 1, 2 - > 
        # potentially an answer

        # eating speed is 1 - >
        # 1, 4 ,3, 3
        # 1 + 4 + 3 +3 - > 11
        # 11 <= 9 - > False
        # NOT AN ANSWER

        # eating speed is 2 - > 
        # 1, 2, 2, 1 # hours it took
        # 3 / 2 -> 1.5  
        # you can not eat from another pile in the same hour.
        # therefor we have to do ceiling division
        # 3 / 2 -> 1.5  round 1.5 up -> 2

        # we add up the hours it took to finish
        #1 +2 + 2 + 1 - > 6 <= 9 -> True

        # return 2 as the answer

        # example Input: piles = [1,4,3,2], h = 9
        # testing out all the eating speeds
        # (1 + 4) // 2  -> 2
        leftPointer = 1
        rightPointer = max(piles)
        answer = float("inf")

        while leftPointer <= rightPointer:
            currentEatingSpeed = (leftPointer + rightPointer) // 2
            # this is our eating speed
            hoursTaken = 0
            # now we have to go through each pile and simulate the eating
            for pile in piles:
                hoursTaken += (pile + currentEatingSpeed  - 1) // currentEatingSpeed
            
            # now we know how many hours it takes for us to finish eating
            # all of the food


            # now we have to check if it is within the limits
            if hoursTaken <= h:
                answer = min(answer, currentEatingSpeed)

                # can we have a faster speed?
                rightPointer = currentEatingSpeed - 1
            
            
            elif hoursTaken > h: #this is not allowed # took too many hours
            # need to increase eating speed
                leftPointer = currentEatingSpeed + 1
        return answer
























