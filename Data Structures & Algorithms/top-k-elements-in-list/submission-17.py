class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to look for the kth most common integers

        numberCounter = defaultdict(int) #key is our number, value is occurances

        # we need to make an list filled with empty lists
        freq = [[] for index in range(len(nums) + 1)]
        # we add another one, because the end is exclusive
        # for example we want to count the freq for 5 
        # we need 6 buckets, the last one not being used


        for number in nums:
            numberCounter[number] += 1

        # now we have to create a list, the index is the number of occurances
        # the number in that index is the number that occured that many times
        # we will make a list of lists

        for number, count in numberCounter.items():
            freq[count].append(number)
        
        result = []

        # we start at the end of freq list, go backwards one at a time
        for index in range(len(freq) - 1, 0, -1):
            for number in freq[index]:
                result.append(number)
                if len(result) == k:
                    return result

            





        