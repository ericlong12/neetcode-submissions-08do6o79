from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return true if they are anagrams
        # otherwise turn false

        # what is an anagram
        # when a word contains the same amount of exect letters

        # sort the word, then use two pointer to match if they are the same

        # use a hashmap

        # dictionary

        # search through each array one, then we check if their dictionarys
        # are the same o(1)
        # going thru array o(n)

        tDict = defaultdict(int)
        sDict = defaultdict(int)
        # run two four loops, one on s one on t

       # 2 * o(n)  -> o(n)
        for letter in s:
            sDict[letter] += 1

        for letter in t:
            tDict[letter] += 1
        
        # o(1)
        if sDict == tDict:
            return True
        else:
            return False









