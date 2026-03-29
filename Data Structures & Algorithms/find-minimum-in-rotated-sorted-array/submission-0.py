class Solution:
    def findMin(self, nums: List[int]) -> int:
        def split_and_order(lst):
            if len(lst) <= 1:
                return [lst]
            mid = len(lst) // 2
            left = split_and_order(lst[:mid])
            right = split_and_order(lst[mid:])
            return sorted(left + right, key=lambda x: x[0])

        result = split_and_order(nums)
        return result[0][0]