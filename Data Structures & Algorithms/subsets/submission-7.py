class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        answer = []

        def dfs(index):
            if index == len(nums):
                return answer


            # we decide to add 
            subset.append(nums[index])
            answer.append(subset.copy())
            dfs(index + 1)

            # this is where we don't add, aka the right subtree
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        answer.append([])
        return answer
        














