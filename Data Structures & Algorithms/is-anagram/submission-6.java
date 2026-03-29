

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> counter1 = new HashMap<>();
        Map<Character, Integer> counter2 = new HashMap<>();

        for (char c : s.toCharArray()) {
            counter1.put(c, counter1.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            counter2.put(c, counter2.getOrDefault(c, 0) + 1);
        }

        return counter1.equals(counter2);
    }
}
