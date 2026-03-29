class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        #we can solve this with two pointers. 

        # we should use a bucket

        leftPointer = 0

        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            bucket = s[leftPointer]
            s[leftPointer] = s[rightPointer]
            s[rightPointer] = bucket
            leftPointer += 1
            rightPointer -= 1
        return s
