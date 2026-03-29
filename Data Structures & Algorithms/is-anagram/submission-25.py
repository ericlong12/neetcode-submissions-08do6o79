class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can solve this by having a letter counter or by ordering

        # create a dictionary, if the dictionary is the same then
        # the key should be the letter, the value is the amt shown.

        dictionaryS = {}
        dictionaryT = {}

        for letter in s:
            dictionaryS[letter] = dictionaryS.get(letter,0) + 1
        

        for letter in t:
            dictionaryT[letter] = dictionaryT.get(letter,0) + 1

        if dictionaryS == dictionaryT:
            return True
        else:
            return False
        

            