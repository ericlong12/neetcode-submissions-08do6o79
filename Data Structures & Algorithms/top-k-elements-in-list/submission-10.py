class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the kths most numbers in the array

        #first we got to make a counter so we can count how often
        # soemething shows up in the llist
        # make a dictionary. the key willll tbe the number the vallue
        # willl be how often that number shows up.
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            elif num in counter:
                counter[num] +=1
        # now we have a dictionary which is fillled with key value pairs
        # the key is the number the value is the amount of occurances
        # nowe we  got to th get the kth llargest numbers
        valueList = sorted(list(counter.values()))
        reversedList = valueList[::-1]

        # right here revered list 
        theMaxValuesNeeded = reversedList[:k]

        theAnswer = set()

        for key, value in counter.items():
            for numTarget in theMaxValuesNeeded:
                if value == numTarget:
                    theAnswer.add(key)
        return list(theAnswer)

        