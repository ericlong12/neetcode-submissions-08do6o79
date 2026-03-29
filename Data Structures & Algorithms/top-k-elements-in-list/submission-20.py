class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we should count how many times a number has shown up

        numberCounter = defaultdict(int)
        for number in nums:
            numberCounter[number] += 1
            # key: 1 value: 1
            # key: 2 value: 2
            # key: 3  value:3
        # number counter is now filled, 


        
        # bucket. each element
        # key: 3 value: 2
        # this means that value 2, has appeared 3 times in our array 

        # key will be from range 0-len(nums)
        # value: will be a list
        
        bucketDictionary = {occur: [] for occur in range(1, len(nums) + 1)}

        # now we should fill up our bucket with number counter
        for number, numberOccur in numberCounter.items():
            bucketDictionary[numberOccur].append(number)
        # bucketDictionary[4] -> 3
        # this means that the number 3 was seen four times in nums



        # we should go though that bucket from most often seen:
        # fill up our result until it becomes size k

        # This implies that we want to go through bucketDictionary backwards
        # bc the biggest number is seen at the end of the dictionary
        result = []
        
        # bucketDictionary[2] : [3,5,6,7,8]


        for index in range(len(nums), 0, -1):
            # we start at the nth index
            # this is a listbucketDictionary[index]
            for index2 in range(len(bucketDictionary[index]) - 1 , -1, -1):
                result.append(bucketDictionary[index][index2])
                if len(result) == k:
                    return result

















