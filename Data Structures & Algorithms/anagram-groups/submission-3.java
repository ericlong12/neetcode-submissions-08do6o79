class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Create a map to store the groups of anagrams
        Map<String, List<String>> anagramMap = new HashMap<>();

        // Iterate through each string in the input array
        for (String s : strs) {
            // Convert the string to a character array and sort it
            char[] characters = s.toCharArray();
            Arrays.sort(characters);
            // Convert the sorted character array back to a string
            String sorted = new String(characters);

            // If the sorted string is not yet a key in the map, add it
            if (!anagramMap.containsKey(sorted)) {
                anagramMap.put(sorted, new ArrayList<>());
            }

            // Add the original string to the list corresponding to the sorted string
            anagramMap.get(sorted).add(s);
        }

        // Return the values of the map as a new list of lists
        return new ArrayList<>(anagramMap.values());
    }
}
