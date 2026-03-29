"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # we are given intervals

        # we know that the integer in index 0 is the starting time
        sortedNumbers = sorted(intervals, key = lambda Interval:Interval.start)

        for index in range(len(sortedNumbers)-1): # we subtract once bc we look into the future here
            if sortedNumbers[index].end > sortedNumbers[index+1].start:
                return False
        return True
    

