class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False


        # permutation will be same size
        # same letter
        s1Count = {} # key: letter,  value: count of the letter
        # we make a dictionay for s1.
        for letter in s1:
            s1Count[letter] = s1Count.get(letter, 0) + 1
        # now we have the count of s1.



        #length of s1 will be the window size
        windowCount = {}
        for index in range(len(s1)):
            windowCount[s2[index]] = windowCount.get(s2[index],0) + 1

            if s1Count == windowCount:
                return True
        

        for rightIndex in range(len(s1), len(s2)):
            windowCount[s2[rightIndex]] = windowCount.get(s2[rightIndex], 0) + 1
            # now we will remove the leftPointer element
            # we get leftPointer position by doing
            # rightIndex - len(s1)
            windowCount[s2[rightIndex - len(s1)]] -= 1
            if windowCount[s2[rightIndex - len(s1)]] == 0:
            # del windowCount[leftChar]
                del windowCount[s2[rightIndex - len(s1)]]

            if s1Count == windowCount:
                return True

        return False





        # the save lookup time, we can 


        # we go thorugh s2 with a sliding window and update
        # its own personal dictionary.

        # each step, we check if s2 dict is equal to s1 dictionary


        # we know the window MUST be size of s1 in order to be
        # a potential answer.
        # therefore we can initilize a window of size len(s1) 
        # and slide it until index is the len(s2)