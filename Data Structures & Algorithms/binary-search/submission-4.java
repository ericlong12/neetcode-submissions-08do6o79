class Solution {
    public int search(int[] nums, int target) {

        // now we should solve in java
        // first have our pointer

        int leftPointer = 0;
        int rightPointer = nums.length - 1;
        int middle;

        while (leftPointer <= rightPointer){
            // we get the middle
            middle = (rightPointer + leftPointer) / 2;

            if (target == nums[middle]) {
                return middle;
            }

            else if (target > nums[middle]) {
                // we should increase
                leftPointer = middle + 1;

            }
            else {
                rightPointer = middle - 1;
            }

        }
        return -1;



        
    }
}
