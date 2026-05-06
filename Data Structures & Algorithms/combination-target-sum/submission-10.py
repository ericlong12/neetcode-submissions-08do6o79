class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        answer = []

        # we make the DFS

        def dfs(index, currentSet, total):
            if total == target:
                answer.append(currentSet.copy())
                return


            # think of the other base case

            # we we are out of bounds

            if index >= len(nums) or total > target:
                return # this is backtracking



            # we add the number and run the dfs

            currentSet.append(nums[index])

            # run the dfs
            dfs(index, currentSet, total + nums[index])

            # now remove

            currentSet.pop()

            # now run dfs again on the next number in nums
            dfs(index + 1, currentSet, total)

        # now we call the dfs

        dfs(0,[],0)
        return answer



            


            






