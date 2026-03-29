class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (uniques.contains(nums[i])){
                return true;
            }
            else{
                uniques.add(nums[i]);
            }
        }
        return false;
    }
}

// to declare a hashset you use Set<Integers> "name of the hashset"