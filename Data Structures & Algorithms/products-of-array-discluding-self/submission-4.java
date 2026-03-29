class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] array = new int[nums.length];
        
        int right = 1, left = 1;

        // Iterate through the array to calculate the product of elements to the left of each index
        for (int i = 0; i < nums.length; i++) {
            array[i] = left;
            left *= nums[i];
        }

        // Iterate through the array backwards to calculate the product of elements to the right of each index
        for (int i = nums.length - 1; i >= 0; i--) {
            array[i] *= right;
            right *= nums[i];
        }
        return array;
    }
}
