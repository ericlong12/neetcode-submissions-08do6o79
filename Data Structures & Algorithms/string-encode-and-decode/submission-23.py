class Solution:
    
    # we are given a list of strings and we want to
    # return a single string of all those strings combined


    def encode(self, strs: List[str]) -> str:
    # go through each string and append it to masterstring
    # we should have # (a symbol) to seperate these words

    #["Hello","World"]
    # 5#Hello 5#World
        masterWord = ""
        for word in strs:
            masterWord += str(len(word)) + "#" + word
        return masterWord


    # edge case is that when we # <- is in the string

    def decode(self, s: str) -> List[str]:
    # For decode we will start at an integer
    # that integer will tell us how many letters our word is
    # we read that integer until we reach our delimiter "#"
        leftPointer = 0
        answerList = []


        while leftPointer < len(s):
            index = leftPointer
            while s[index] != "#":
                index += 1 #increments left pointer until it reaches #
                # we can now grab the length of the word
            lengthOfWord = int(s[leftPointer:index])

                # now that we have the length of the word. lets get the word itself

            leftPointer = index + 1 #this is the start of the word
                # we we append the the result
            answerList.append(s[leftPointer:leftPointer+int(lengthOfWord)])

            leftPointer = leftPointer + int(lengthOfWord) # might be out of index

        return answerList





