class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # left side will be to add the number
        #rightside will be to leave number out

        answer = []

        def dfs(index, currentSubset, total):
            if total == target:
                answer.append(currentSubset.copy())
                return
            

            # if it is out of bounds we want to backtrack

            if index >= len(nums) or total > target:
                return

            
            # the other conditons are if we still have to add up
            # to reach the target number

            currentSubset.append(nums[index])
            # we added the number to the subset
            dfs(index, currentSubset, total + nums[index])


            # for the right side we want to remove

            currentSubset.pop()
            dfs(index + 1, currentSubset, total)
        
        dfs(0, [], 0)

        return answer




















