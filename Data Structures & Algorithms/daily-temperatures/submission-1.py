class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we should make use of a stack
        # can use stack to track the biggest number
        # input temperatures = [30,38,30,36,35,40,28]
        # stack = [[38, 1], [30, 2], ]


        # have the stack hold the largest number on the right
        stack = []
        answer = [0] * len(temperatures)
        for index in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[index],index])
            
            else:
                while stack and stack[-1][0] <  temperatures[index]:
                    answer[stack[-1][1]] = (index - stack[-1][1]) # an integer
                    stack.pop()
                    
                stack.append([temperatures[index],index])


        return answer

                
