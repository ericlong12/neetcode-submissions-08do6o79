

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {  // Corrected for loop
            set.add(num);
        }
        
        int longestStreak = 0;

        for (int number : set) {  // Corrected for loop
            if (!set.contains(number - 1)) {
                int currentNum = number;
                int currentStreak = 1;
                
                // Moved the while loop inside the if block
                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                if (currentStreak > longestStreak) {
                    longestStreak = currentStreak;
                }
            }
        }

        return longestStreak;  // Moved the return statement outside the for loop
    }
}
