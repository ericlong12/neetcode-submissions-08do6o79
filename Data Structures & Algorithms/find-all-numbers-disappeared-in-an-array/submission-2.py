class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # you are given an array and you have to find the numbers which are not in the range from 1 to length of nums


        n = len(nums)

        # we should mark everything which is spotted

        # whatever index is not there is the one that is missing

        # we can do this the easy way

        answer = set(range(1,n + 1))
        # that creates a set from 1 to length of nums

        for number in nums:
            answer.discard(number)


        return list(answer)