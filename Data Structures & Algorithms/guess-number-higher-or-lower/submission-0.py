# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # we have an api which is called guess, it returns an int
        # we give it an in it returns an int

        # I see, the max number is n

        leftPointer = 0
        rightPointer = n + 1


        while leftPointer <= rightPointer:
            middle = (leftPointer + rightPointer) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                rightPointer = middle - 1
            elif guess(middle) == 1:
                leftPointer = middle + 1
                