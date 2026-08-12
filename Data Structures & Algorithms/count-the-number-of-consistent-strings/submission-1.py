class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # we count number of words which fit out list

        allowedSet = set(allowed)
        answer = 0

        for word in words:
            itWorks = True
            for letter in word:
                if letter not in allowedSet:
                    itWorks = False
                    break

            # this is for every word
            if itWorks:
                answer += 1
        
        return answer

