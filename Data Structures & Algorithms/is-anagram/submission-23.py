class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ListA = sorted(list(s))
        ListB = sorted(list(t))
        return ListA == ListB
        
        