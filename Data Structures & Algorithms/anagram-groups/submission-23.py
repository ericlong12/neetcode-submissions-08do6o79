class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary. defautdict(llist)
        dictionaryAnagram = defaultdict(list)

        # Thhhis dictionary shoulld have sorted word. the values list
        #shhould be the actual word
        for word in strs:
            # add the word into the dictionary if not there yet
            # do this by append
            sortedWord = "".join(sorted(word))
            dictionaryAnagram[sortedWord].append(word)
        return list(dictionaryAnagram.values())