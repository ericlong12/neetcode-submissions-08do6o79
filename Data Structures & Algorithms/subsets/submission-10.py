class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        answer = []

        def dfs(index):
            if index == len(nums):
                answer.append(subset.copy())
                return


            # we decide to add 
            subset.append(nums[index])
            dfs(index + 1)

            # this is where we don't add, aka the right subtree
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return answer
        














