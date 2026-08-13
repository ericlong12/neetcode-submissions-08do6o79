class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # we are trying the hashmap solution

        answer = 0
        seenSet = defaultdict(int)


        for number in nums:
            answer += seenSet[number]
            seenSet[number] += 1
        
        return answer
            
