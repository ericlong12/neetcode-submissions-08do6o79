class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topPointer = 0
        bottomPointer = ROWS - 1


        while topPointer <= bottomPointer:
            currentRow = (topPointer + bottomPointer) // 2

            if target < matrix[currentRow][0]:
                bottomPointer = currentRow - 1

            elif target > matrix[currentRow][-1]:
                topPointer = currentRow + 1

            else:
                break
        currentRow = (topPointer + bottomPointer) // 2

        if topPointer > bottomPointer:
            return False

            # we are in the right row
        # we can now assume that we are in the right row:

        leftPointer = 0
        rightPointer = COLS - 1

        #currentRow is the correct row
        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2
            if target < matrix[currentRow][middlePointer]:
                rightPointer = middlePointer - 1
            
            elif target > matrix[currentRow][middlePointer]:
                leftPointer = middlePointer + 1
            
            else:
                return True
        return False
        















