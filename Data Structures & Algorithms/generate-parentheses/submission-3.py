class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking here

        answer = []

        def dfs(openB,closeB, current):
            if closeB == n and openB == n:
                answer.append(current)
                return
            
            # instead of randomly adding openB, check if we can

            if openB < n:
                dfs(openB+1, closeB, current + ("("))

            if closeB < openB:
                # then we can add it
                current = current + ")"
                closeB += 1
                dfs(openB, closeB, current)

        dfs(0,0,"")
        return answer








