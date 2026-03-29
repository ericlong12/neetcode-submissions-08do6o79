class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we are given a bunch of words
        # group them if they are anagrams of each other

        #make a dictionary for them all. 
        # if they have the same then put them into an array of an array

        dictionary = defaultdict(list) #key = letter, value = number of occurances

        # we are given a list of strings,
        for string in strs:
            # this creates a counter for each letter in the string
            # for example this one will have a list with 26 zeros
            count = [0] * 26

            # now we go through each letter in the string
            for character in string:
                #this updates our list named count, index 1 = b
                count[ord(character) - ord('a')] += 1

            # this updates out dictionary, our key is a tuple
            # our value is the string which made the tuple
            # the tuple itself is the count of each letter shown.
            dictionary[tuple(count)].append(string)

        return list(dictionary.values())
                