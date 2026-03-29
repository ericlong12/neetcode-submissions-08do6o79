class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary. you will be solving this question
        # by working on using ord() this method turns letters
        #to it orginal posion using a numbver we subtract 'a' so
        # we know  how far away it is from th rest

        # creates a dictionary which will take in list as a asset
        dictionary = defaultdict(list)

        # loop through every word in the list to count its letters
        for word in strs:
            #count is a list. one 0 is initilized for each letter
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                # add this to the count list that you made eariler
                count[index] += 1

                # now you have sucessfully counted each letter in the word
                # and put this in a list. the index 0 is equal to a etc

                # the value of our dictionary is the word
                # the key for our dictionary is our list of letters.
            dictionary[tuple(count)].append(word)
        return list(dictionary.values())
