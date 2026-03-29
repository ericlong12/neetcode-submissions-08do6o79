class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] monkeyBlack = new int[26];

        for (int i = 0; i < s.length(); i++) {
            //use charAt. method
            monkeyBlack[s.charAt(i) - 'a']++;
            monkeyBlack[t.charAt(i) - 'a']--;
        }

        for (int number : monkeyBlack) {
            if (number != 0) {
                return false;
            }
            
            
        }
        return true;


    }
}
