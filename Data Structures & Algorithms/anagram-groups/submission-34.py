class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary which hold key = tuple of letters value = the word itself

        # first make a list dictionary
        dictionary = defaultdict(list)

        # now go through each word in str
        for word in strs:
            # make a list to hold each letter. alphabet has 16 letters
            count = [0] * 26
            
            # now we read each letter in the word to put them in the list
            for letter in word:
                index = ord(letter) - ord("a")

                # now that we have the index of the letter. we put it inside our list

                count[index] += 1
                
                # this list has the number of occurances that the letter shows up, the index
                # of the number corralates to the letter

            # now that we have done this for every letter in the word.
            # we will now add this word to our dictionary
            dictionary[tuple(count)].append(word)
        # now that we havev done this for every word in the dictionary.
        # we not return the value for each key in the dictionary
        return list(dictionary.values())
    