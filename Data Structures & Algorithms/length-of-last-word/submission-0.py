class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # we can use pointers instead

        rightSidePointer = len(s) - 1
        answer = 0

        while rightSidePointer >= 0 and s[rightSidePointer] == " ":
            rightSidePointer -= 1

        while rightSidePointer >= 0 and s[rightSidePointer] != " ":
            rightSidePointer -=1
            answer += 1
        return answer