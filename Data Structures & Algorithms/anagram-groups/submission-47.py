class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord a -> 20
        dictionary = defaultdict(list)

        for word in strs:
            counter = [0] * 26

            for letter in word:
                     #b = 21.  #a = 20
                ourIndex = ord(letter) - ord("a")
                counter[ourIndex] += 1
            #[2,0,0] -> aa

            dictionary[tuple(counter)].append(word)

        # we have a dictionary key:[2,0,0] value: ["act", "cat"]

        result = []

        for values in dictionary.values():
            result.append(values)
        
        return result
        


