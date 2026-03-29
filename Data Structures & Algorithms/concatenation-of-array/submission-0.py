class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = nums.copy()

        for number in nums:
            answer.append(number)


        return answer
        