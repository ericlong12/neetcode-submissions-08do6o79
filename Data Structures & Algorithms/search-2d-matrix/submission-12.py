class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr= []
        for row in matrix:
            arr.extend(row)
        
        left = 0
        right = len(arr) - 1


        while left <= right:
            middlePointer = (left + right) // 2
            
            if arr[middlePointer] < target:
                left = middlePointer + 1

            elif arr[middlePointer] > target:
                right = middlePointer - 1

            else:
                return True
        return False