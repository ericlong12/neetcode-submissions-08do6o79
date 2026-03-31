class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer= []
        subset = []


        def dfs(index):
            if index == len(nums):
                answer.append(subset.copy())
                return

            
            # this is we add a number
            subset.append(nums[index])
            dfs(index + 1)


            # we don't add the number
            subset.pop()
            dfs(index + 1)

        dfs(0)




        return answer