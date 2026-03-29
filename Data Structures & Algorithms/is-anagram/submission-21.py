class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedSetOne = sorted(s)
        sortedSetTwo = sorted(t)

        myList1 = list(sortedSetOne)
        myList2 = list(sortedSetTwo)

        if (myList1 == myList2):
            return True
        else:
            return False
        