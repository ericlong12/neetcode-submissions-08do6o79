class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we should use sliding window to solve

        # dictionary to count letters 

        # we want to get the letter with the highest count.

        # we get the length of our window.
        # slowingWindow length - highestLetter Count

        # updated max count
        # we do this til we have seen all of the substring

        # return the answer, maxCount

        longestSubstring = 0
        leftPointer = 0

        letterCount = {}
        
        # we should go through the string

        # we have to have a counter to make sure it doesn't exceed k
        for index in range(len(s)):
            # this is like defaultdict.
            # it gets the letter at this key,
            # if it isn't there, its 0, add 1 regarless
            letterCount[s[index]] = letterCount.get(s[index], 0) + 1

            maxValue = max(letterCount.values())
            sumValue = sum(letterCount.values())

            replacementsNeeded = sumValue - maxValue
            
            while replacementsNeeded > k:
                # we want to remove the letter from the dictionary
                letterCount[s[leftPointer]] -= 1
                leftPointer += 1

                maxValue = max(letterCount.values())
                sumValue = sum(letterCount.values())
                replacementsNeeded = sumValue - maxValue
            
            longestSubstring = max(longestSubstring,index - leftPointer + 1 )

        return longestSubstring






















