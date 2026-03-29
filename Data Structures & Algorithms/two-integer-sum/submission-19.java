class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        //find the value needed to solve the equation aka given x find y for x + y = z
        for (int i=0; i<nums.length; i++){
            int difference = target - nums[i];

            if (map.containsKey (difference)){
                return new int[] {map.get(difference), i};
            }
            else{
                map.put(nums[i],i);
            }
        }
        return new int[] {};
        // check if the hashmap has the differnce inside of it. if not then add the current number

        
    }
}
