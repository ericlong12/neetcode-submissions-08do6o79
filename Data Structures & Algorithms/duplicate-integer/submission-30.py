class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can make a set here
        dupeSet = set()

        for number in nums:
            if number in dupeSet:
                return True
            else:
                dupeSet.add(number)
        return False

        