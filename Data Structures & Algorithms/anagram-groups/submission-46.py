class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap solution
        dictionaryOrderedWordToRegularWord = defaultdict(list)
        for word in strs:
            # each word should have their on array
            alphabet = [0] * 26
            for letter in word:
                                # 52. c        #50 a
                indexPosition = ord(letter) - ord("a")
                alphabet[indexPosition] += 1
            orderedWord = tuple(alphabet)
            dictionaryOrderedWordToRegularWord[orderedWord].append(word)

        answer = []

        for values in dictionaryOrderedWordToRegularWord.values():
            answer.append(values)

        return answer






