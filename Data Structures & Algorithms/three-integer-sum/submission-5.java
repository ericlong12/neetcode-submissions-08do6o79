class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // sort the array so we can find duplicates
        Arrays.sort(nums);

        // make a list of list integers
        List<List<Integer>> res = new ArrayList<>();

        // loop through the whole array of nums
        for (int i = 0; i < nums.length; i++) {
            // we make this line of code because we are looping through the list
            // from left to right, and the array is sorted in acending order
            // which if nums[i] is greater than 0, then we can only make positive numbers
            // from there on.
            // this is not ideal because we are trying to make the sum of 3 numbers equal 0
            if (nums[i] > 0 ) break;

            // this line of code is used to skip over duplicate elements
            // keep in mind this is a sorted array
            // if there are duplicate elements then this loops skips the current iteration
            if (i > 0 && nums[i] == nums[i-1]) continue;

            // here we make 2 pointers
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) {
                    right--;
                }
                else if (sum < 0) {
                    left++;
                }
                else {
                    // if the sum equals exactly 0 then we add these numbers to our result list
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;

                    // after adding them to our list we search the rest of our array
                    left++;
                    right--;

                }
            }


        }
        return res;

        
    }
}
