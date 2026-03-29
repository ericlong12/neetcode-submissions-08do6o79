class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> answer = new HashMap<>();
        for (String word : strs){
            int[] counter = new int[26];
            for (char letter :word.toCharArray()){
                counter[letter - 'a']++;
            }
        
            String wordID = Arrays.toString(counter);
            if (!answer.containsKey(wordID)){
                // puts the wordID into the HashMap, and makes its value an empty ArrayList
                answer.put(wordID, new ArrayList<>());
            }
            answer.get(wordID).add(word);

     }
     return new ArrayList<>(answer.values());
    }
}
