class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currentSubset = []
        answer = []



        def dfs(index): # this will be 0 at first

            # write down the base case

            if index == len(nums):
                answer.append(currentSubset.copy())
                return



            # one condition is to add
            currentSubset.append(nums[index])
            dfs(index + 1)

            # the other condition is to not add the number

            currentSubset.pop()
            dfs(index + 1)
        
        dfs(0)


        return answer



















