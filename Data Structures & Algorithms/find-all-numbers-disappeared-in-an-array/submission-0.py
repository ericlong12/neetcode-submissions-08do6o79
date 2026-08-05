class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #think of this like a linked list, we try to traverse it.

        # we should first start with a loop to mark all of the numbers
        # in the array as visited, then we mark them all again as seen

        n = len(nums)

        answer = set(range(1,n + 1))
        # a set starts on the first number and leaves the last number excluded

        for number in nums:
            if number in answer:
                answer.discard(number)
        
        return list(answer)