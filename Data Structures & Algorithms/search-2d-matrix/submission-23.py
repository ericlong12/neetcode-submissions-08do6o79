class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixToArray = []

        for row in matrix:
            matrixToArray.extend(row)
        
        # now we have a long array

        leftPointer = 0
        rightPointer = len(matrixToArray) - 1


        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2

            if matrixToArray[middlePointer] == target:
                return True
            elif matrixToArray[middlePointer] < target:
                leftPointer = middlePointer + 1

            elif matrixToArray[middlePointer] > target:
                rightPointer = middlePointer - 1
        return False
        




