class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigDictionary = defaultdict(list)
        for word in strs:
            sortedWord = sorted(word)
            bigDictionary[tuple(sortedWord)].append(word)

        # after finishing this loop we have a dictionary 
        # with key : sorted word, value: word itself

        answers = []

        for values in bigDictionary.values():
            answers.append(values)


        return answers




            