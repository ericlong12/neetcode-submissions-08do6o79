class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we have to find the longest substring which doesnt
        # repeating chars
        
        leftPointer = 0
        lengthOfString = len(s)
        iSawIt = set()
        maxLength = 0
        # use a while loop to keep on popping.
        for index in range(lengthOfString):
            while s[index] in iSawIt:
                iSawIt.remove(s[leftPointer]) # we have the assumption that everything in leftPointer as already been see
                leftPointer += 1
            
            # then is not in the index
            iSawIt.add(s[index])
            maxLength = max(maxLength, len(iSawIt))
        return maxLength

