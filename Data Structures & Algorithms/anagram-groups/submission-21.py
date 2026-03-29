class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}

        for word in strs:
            # Initialize a count of 26 zeros (for 'a' to 'z')
            count = [0] * 26
            for char in word:
                # Increment the count for this character
                count[ord(char) - ord('a')] += 1

            # Use the tuple of counts as the dictionary key
            key = tuple(count)

            # Group the word by its anagram signature
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)

        return list(anagram_map.values())
