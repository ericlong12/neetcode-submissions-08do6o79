class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solve this question using a set and checking if element is already in set
        # if it is already in set then remove it and increment the left pointer
        # if it is not in set then increment the right pointer

        # set up our variables we will use for the problem
        seen = set()
        left = 0
        maxLength = 0

        #MENTAL NOTE
        # you don't have to use the lef pointer right away, that way it doesn't come to the case where
        # left and right pointer are in the same position. 

        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1

            else:
                seen.add(s[right])
                maxLength = max(maxLength, right - left + 1)
        return maxLength

