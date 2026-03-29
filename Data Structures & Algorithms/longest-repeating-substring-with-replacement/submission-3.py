from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we can change up to k elements
        # return the length of the substring

        # have a counter, shows how many times an element has shown
        # up in the current window

        dictionaryCounter = defaultdict(int)

        leftPointer = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            dictionaryCounter[s[right]] += 1

            # now we get the higest frequencey in the window
            max_freq = max(dictionaryCounter.values())

            #check if the window is invalid
            while right - leftPointer + 1 - max_freq > k:
                # this is invalid, increase leftPointer
                dictionaryCounter[s[leftPointer]] -= 1
                leftPointer += 1
            
            answer = max(answer, right - leftPointer + 1)
            


        return answer
            #update answer



       