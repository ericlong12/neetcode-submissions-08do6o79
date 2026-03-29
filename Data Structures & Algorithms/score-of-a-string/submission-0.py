class Solution:
    def scoreOfString(self, s: str) -> int:
        # current - previous
        result = 0

        for index in range(len(s) - 1):
            result += abs(ord(s[index]) - ord(s[index + 1]))
        return result