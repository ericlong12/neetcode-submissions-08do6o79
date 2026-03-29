class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we are given two arrays. speed and position. we should merge
        # pair is an array
        # in this array we insert position and speed
        pair = [(pos,spd) for pos,spd in zip(position,speed)]
        
        # now we sort the array based on size. we start from the biggest
        # position, because we care about the big position first

        pair.sort(reverse = True)

        # now we make a stack to get the amt of fleets
        stack = []

        for position, speed in pair:
            stack.append((target-position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        