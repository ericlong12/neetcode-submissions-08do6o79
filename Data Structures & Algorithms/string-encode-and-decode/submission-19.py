class Solution:
    
    # we are given a list of strings:
    # we want to return the list of string into one string
    # thats all, we don't have to encrypt
    def encode(self, strs: List[str]) -> str:
        codeWord = ""
        for string in strs:
            lengthOfString = len(string)
            codeWord += str(lengthOfString) + "#" + string
        return codeWord

        

    def decode(self, s: str) -> List[str]:
        # now we have to decode
        answer = []
        leftPointer = 0


        while leftPointer < len(s):
            rightPointer = leftPointer
            while s[rightPointer] != "#":
                rightPointer += 1
            length = int (s[leftPointer:rightPointer])
                # now were are at the start of the string
            leftPointer = rightPointer + 1

                # right pointer is now at the next hashtag
            rightPointer = leftPointer + length
            answer.append(s[leftPointer:rightPointer])
            leftPointer = rightPointer
        return answer





