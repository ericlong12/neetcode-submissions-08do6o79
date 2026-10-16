class Solution {
    public int search(int[] nums, int target) {
        
        // make the calls
        int leftPointer = 0;
        int rightPointer = nums.length - 1;
        int middle;


        while (leftPointer <= rightPointer){
            middle = (leftPointer + rightPointer) / 2;


            if (target == nums[middle]) {
                // then we return the index
                // we reached the answer
                return middle;

            }

            else if (target > nums[middle]) {
                // we need to increase the number to reach target
                leftPointer = middle + 1;




            }

            else {
                rightPointer = middle - 1;
            }

        // otherwise we can just return -1 if its not the answer




        }

        // outside the loop now
        return -1;
    }
}
