class Solution:
    def isValid(self, s: str) -> bool:
        #make a hashmap. the key is the closing bracket
        # if it is not in the hashmap, then add it to the stack.
        # check if the stack is empty, if it is not then return false
        dictionary = {"}":"{", "]":"[", ")":"("}

        # testing () {} []

        # create a stack
        stack = []
        # we start with a single string.
        for letter in s:
            if letter in dictionary:
                if stack and stack[-1] == dictionary[letter]:
                    stack.pop()
                else: return False
            else:
                stack.append(letter)

        if stack:
            return False
        else: return True
        


