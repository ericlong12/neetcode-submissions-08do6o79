class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary_list = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            print(sortedWord)
            dictionary_list[sortedWord].append(word)
        
        return list(dictionary_list.values())

        