class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                answer.append(subset.copy())
                return
            
            # if we want to include nums[i]
            subset.append(nums[index])
            dfs(index+1)

            # if we don't want to include nums[index]
            subset.pop()
            dfs(index+1)

        dfs(0)
        return answer
