class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack. Calculate the distance between
        # the top of the stack to the end of the stack
        # subtract when you see that the last element
        # is greater than the elements before it. 


        # al already know the length of the array for the result
        # go ahead and fill it out

        result = [0] * len(temperatures)
        
        # our stack will hold an array filled with lists temperature:index
        stack = []

        for index, temperature in enumerate(temperatures):
            # now we have to check if the current element is bigger than the last one
            while stack and temperature > stack[-1][0]:
                stackTemperature,stackIndex = stack.pop()

                # this gets the smallest index, far left - the biggest index
                # this saves into a result,
                # we access the result's index at index [stackIndex]
                result[stackIndex] = index - stackIndex
            stack.append((temperature,index))
        return result
