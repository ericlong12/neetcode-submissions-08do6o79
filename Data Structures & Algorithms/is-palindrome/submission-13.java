class Solution {
    public boolean isPalindrome(String s) {
        List<Character> listOfCharacters = new ArrayList<>();

        for (char character : s.toCharArray()) {
            if (Character.isLetterOrDigit(character)){
                listOfCharacters.add(Character.toLowerCase(character));
            }
        }
        List<Character> listOfCharactersReversed = new ArrayList<>();

        for (int i = listOfCharacters.size() - 1; i >= 0; i--) {
            
            listOfCharactersReversed.add(listOfCharacters.get(i));
        }

        StringBuilder reversedString = new StringBuilder(listOfCharactersReversed.size());
        for (Character ch : listOfCharactersReversed) {
            reversedString.append(ch);
        }
        StringBuilder originalString = new StringBuilder(listOfCharacters.size());
        for (Character ch : listOfCharacters) {
            originalString.append(ch);
        }


        if (reversedString.toString().equals(originalString.toString())) {
            return true;
        }
        else {
            return false;
        }
        
    }
}
