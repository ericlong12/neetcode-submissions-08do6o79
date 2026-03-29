class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # an anagram means thes the same frontwards and backwards

        # we can search the middle of the array then spread from there

        # we return true of they are anagrams

        # we can sort the anagram, but that is log n

        # we can do this better with a hashmap

        # we if count the same amount of letter, then it is an anagram

        # we can count letter with dictionary

        characterCounter = defaultdict(int)

        def characterToDictionary(word) -> dictionary:
            characterCounter = defaultdict(int)
            for character in word:
                characterCounter[character] +=1
            return characterCounter

        if characterToDictionary(s) == characterToDictionary(t):
            return True
        
        return False
            