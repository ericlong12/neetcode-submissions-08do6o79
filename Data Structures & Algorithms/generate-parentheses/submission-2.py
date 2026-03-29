class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return all the differnt types of pairs
        # use a stack
        # open always has to be bigger than closing

        stack = []

        result = []

        # we solve this question recursively
        def backtrack(openBracket, closeBracket):
            if openBracket == n:
                if closeBracket == n:
                    result.append("".join(stack))
                    return result
            
            if openBracket < n:
                stack.append("(")
                backtrack(openBracket + 1, closeBracket)
                stack.pop()


            if closeBracket < openBracket:
                stack.append(")")
                backtrack(openBracket, closeBracket + 1)
                stack.pop()
            
        backtrack(0,0)
        return result


        




        