class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we are given two numbers
        # then we are given the mathematical operation
        # that needs to be done


        # we have to output the final answer

        stack = []

        mathSet = set(["+", "-", "*", "/"])

        #token is a bunch of interger and symbols
        # it is either in mathSet, or its an integer.

        for token in tokens:
            if token in mathSet:
                firstInteger = int(stack.pop())
                secondInteger = int(stack.pop())

                if token == "-":
                    temp = secondInteger - firstInteger
                    stack.append(temp)

                elif token == "*":
                    temp = secondInteger * firstInteger
                    stack.append(temp)           

                elif token == "+":
                    temp = secondInteger + firstInteger
                    stack.append(temp)


                elif token == "/":
                    temp = secondInteger / firstInteger
                    stack.append(temp)
        
            else:
                stack.append(token)

        return int(stack[-1])

        
