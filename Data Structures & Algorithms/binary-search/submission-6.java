class Solution {
    public int search(int[] nums, int target) {

        int leftPointer = 0;
        int rightPointer = nums.length - 1;

        int middle;

        while (leftPointer <= rightPointer){
            middle = (leftPointer + rightPointer) / 2;

            if (target == nums[middle]) {
                return middle;
            }

            else if (target > nums[middle]) {
                // we need to increase the middle number
                leftPointer = middle + 1;
            }

            else {
                rightPointer = middle - 1;
            }

        // return -1 if there is never a match
        }
        return -1;



        
    
}
}
