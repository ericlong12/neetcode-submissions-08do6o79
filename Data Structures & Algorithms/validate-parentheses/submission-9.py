class Solution:
    def isValid(self, s: str) -> bool:
        # ( )
        # { }
        # [ ]

        # ( [ ) ] THIS IS NOT VALID

        # if we are given ) we should expect ( to be
        # on top of the stack. else, it is False

        dictionaryBracket = { "}" : "{", ")":"(", "]":"["
        }
        # stack
        stack = []
        openBracket = set()

        openBracket.add("(")
        openBracket.add("[")
        openBracket.add("{")


        for bracket in s:
            if bracket in openBracket:
                stack.append(bracket)

            if bracket not in openBracket:
                if not stack:
                    return False
                popped = stack.pop()
                if popped not in openBracket:
                    return False
                if popped != dictionaryBracket[bracket]:
                    return False

        if not stack:
            return True
        else:
            return False



