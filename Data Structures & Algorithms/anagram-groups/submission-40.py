class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        # this is basically creating a dictonary
        # this dictionary has a key of a list, and an empty list as the value

        # the key of a dicationay must be Immutable. therefore we use a tuple
        for word in strs:
            characterCounter = [0] * 26
        # we set this counter up because it is to identify each letter
            for character in word:
                characterCounter[ord(character) - ord("a")] += 1
            result[tuple(characterCounter)].append(word)
        return list(result.values())

