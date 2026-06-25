class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # okay now we have to find if a string is an anagram of each other. 
        # this means they use the same amount of letters

        counterS = defaultdict(int)
        counterT = defaultdict(int)
        # we make a dictionary for each of the strings and compare them

        # now we fill up the counters

        for letter in s:
            counterS[letter] += 1

        for letter in t:
            counterT[letter] += 1

        return counterS==counterT

