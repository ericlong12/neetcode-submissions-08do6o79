class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we have to ignore the cases
        # we have to ignore the symbols

        # we have function called lower

        # char.isalnum
        # lower()

        # one pointer on left
        # one pointer on right

        # when pointers are equal to each other, we can exit loop

        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            if s[leftPointer].isalnum():
                if s[rightPointer].isalnum():
                    if s[leftPointer].lower() == s[rightPointer].lower():
                        leftPointer += 1
                        rightPointer -= 1
                    else:
                        return False
                else: 
                    rightPointer -= 1
            else:
                leftPointer += 1
        return True
