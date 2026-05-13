class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we return subsets

        result = []
        nums.sort()
        def dfs(index, current):
            #this is the base case
            if index == len(nums):
                result.append(current.copy())
                return
            

            # this is the choice to add it

            current.append(nums[index])
            # we added it to subset.
            dfs(index + 1, current)


            #now we make the choice not to add it

            current.pop()

            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                # we want to skip this one
                index = index + 1
            dfs(index + 1, current)
            
        dfs(0 , [])
        return result








            
