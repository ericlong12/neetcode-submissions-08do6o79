class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // make a new hashMap which takes in int as both key and value
        Map<Integer,Integer> count = new HashMap<>();
        // makes an array which takes in a list of integers per element
        // This is the same as making buckets for each of the elements in nums
        List<Integer>[] freq = new List[nums.length + 1];

        // iterate through the whole array of freq
        // for each index in freq insert an array
        for (int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }
        // update the hashMap with how many times the int was seen in the given array
        // this is done by going through each element in the array nums
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) +1);
        }

        // the value holds the count of the int
        // the key is the int itself

        // freq is an array where each element is a list which carries int

        // freq is acessing index[entry.getValue],
        // which is the amount of times an int shows up on the list

        // then it adds the int into the list. using add(entry.getKey())

        //this while code summarized is that we acess the array freq at postion[frequencey of the int] and insert[int]
        for (Map.Entry<Integer, Integer> entry : count.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }


        // a new int array is made named res and is size k
        int[] res = new int[k];

        int index = 0;
        
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]){
                res[index++] = n;
                if (index == k){
                    return res;
                }
            }
        }


        // this return statement is activated when k = 0;
        return res;



        

    }
}


// keep in mind for this solution we do not care the exact times the int has showed up 
// in the given array. but we only care about the most.
// an analogy would be how we don't care about how smart we are.
// we just care that we are smarter than our classmates. 


