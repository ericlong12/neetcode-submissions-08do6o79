class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // for pointers we should set them to index, not the value at the index.
        int leftPointer = 0;
        int rightPointer = numbers.length - 1;


        while (true){
            int sum = numbers[leftPointer] + numbers[rightPointer];

            if (sum == target) {
                return new int[]{leftPointer+1, rightPointer+1};
            }

            else if (sum > target) {
                rightPointer--;
            }
            else if (sum < target) {
                leftPointer++;
            }






        }

        
    }
}
