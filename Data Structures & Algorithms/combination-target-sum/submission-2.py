class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = [] # we should add the current list to this if it sums up


        # we should have 3 condtions for solving the regression trees
        # choices
        # constraints
        # goals

        # the choice we have in this question is, to add a number or to not

        # the contraint is: is the number bigger than target?

        # goal: get the number to equal the target

        # we should break the problem down. if we are getting closer to 
        # the answer, then we should call itself until we reach the answer

        # integer is the current integer we are at
        # current is the list of integers we have currenty
        # targetSum is the sum of all the current integers

        def dfs(index, current, total):
            # we come with the choices

            # case one is that we add it

            # this is our goal, we want to make total ==. target
            if total == target:
                answer.append(current.copy())
                return # we return because we want to exit the current branch
            
            # this is the constraints
            if index >= len(nums) or total > target:
                return

            
            else:
                # choices. this is where we can either add or ignore the number
                current.append(nums[index])
                dfs(index, current, total + nums[index]) # we added the index
                # we will add it again

                current.pop()
                dfs(index+1, current, total)
        # now we just call it
        dfs(0, [], 0)
        return answer
            












