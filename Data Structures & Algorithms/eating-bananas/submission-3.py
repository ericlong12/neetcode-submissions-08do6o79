from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(k: int) -> int:
            # sum of ceil(p/k) without floats
            return sum((p + k - 1) // k for p in piles)

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                # mid works → try smaller speeds
                right = mid
            else:
                # mid too slow → need bigger k
                left = mid + 1

        return left
