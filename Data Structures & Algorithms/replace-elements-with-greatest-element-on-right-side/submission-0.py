class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggestNumber = -1
        lengthOfArray = len(arr)

        for index in range(lengthOfArray-1,-1,-1):
            bucket = arr[index]
            arr[index] = biggestNumber
            biggestNumber = max(biggestNumber, bucket)


        return arr


