class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n

        def dfs(index):

            if index == n:
                return True

            elif index > n:
                return False
                
            if cache[index] != -1:
                return cache[index]

            cache[index] = dfs(index + 1) + dfs(index + 2)

            return cache[index]
        
        return dfs(0)