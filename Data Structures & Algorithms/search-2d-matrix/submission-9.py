class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check first and last index of each row,


    
        for row in matrix:
            firstElement = row[0]
            lastElement = row[-1]
            if target >= firstElement and target <= lastElement:
                leftPointer = 0
                rightPointer = len(row) - 1

                while leftPointer <= rightPointer:
                    middle = (leftPointer + rightPointer) // 2
                    if row[middle] == target:
                        return True
                    elif row[middle] > target:
                        rightPointer = middle - 1
                    elif row[middle] < target:
                        leftPointer = middle + 1
        return False


