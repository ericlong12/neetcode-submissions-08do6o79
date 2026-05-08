class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()


        def dfs(index, subset, total):
            # now we list the base case
            if total == target:
                answer.append(subset.copy())
                return

            if total > target:
                # if so then we shall backtrack
                return

            
            for index2 in range(index, len(candidates)):
                if index2 > index and candidates[index2] == candidates[index2 - 1 ]:
                    continue

                # we are adding the current index
                subset.append(candidates[index2])
                dfs(index2 + 1, subset, total + candidates[index2])
                subset.pop()
           


            # we can now assume that we are building closer to our target
            # we should have an option to add or not to add the current index





        dfs(0,[],0)

        return answer












            















