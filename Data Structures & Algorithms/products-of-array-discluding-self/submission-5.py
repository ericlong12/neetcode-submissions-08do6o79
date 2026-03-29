class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # one solution could be to create a list. then pop the current element.
        # then add the rest of them.
        currAns = 1
        currList = []
        answer = []
        for i in range(len(nums)):
            currList = []
            for num in nums:
                currList.append(num)
            # now you have a list of nums
            del currList[i]

            for num in currList:
                currAns *= num
            answer.append(currAns)
            currAns = 1
        return answer
