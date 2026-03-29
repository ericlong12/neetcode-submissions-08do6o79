class Solution {
    public boolean isAnagram(String s, String t) {
        List<Character> charList1 = new ArrayList<>();
        List<Character> charList2 = new ArrayList<>();
        for (int i = 0; i < s.length(); i++){
            charList1.add(s.charAt(i));
        }
        for (int i = 0; i < t.length(); i++){
            charList2.add(t.charAt(i));
        }
    Collections.sort(charList1);
    Collections.sort(charList2);

    if (charList1.equals(charList2)){
        return true;
    }
    return false;
    }
}
