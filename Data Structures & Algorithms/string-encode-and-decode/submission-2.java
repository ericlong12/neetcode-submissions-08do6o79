class Solution {

    // Encodes a list of strings to a single string
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String word : strs) {
            for (char letter : word.toCharArray()) {
                char encodedChar = (char) (letter + 10);
                sb.append(encodedChar);
            }
            sb.append((char) 257);  // Using a non-ASCII character as a delimiter
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings
    public List<String> decode(String str) {
        List<String> decodedList = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char letter : str.toCharArray()) {
            if (letter == (char) 257) {  // Check for delimiter
                decodedList.add(sb.toString());
                sb = new StringBuilder(); // Start a new string
            } else {
                char decodedChar = (char) (letter - 10);
                sb.append(decodedChar);
            }
        }
        return decodedList;
    }
}
