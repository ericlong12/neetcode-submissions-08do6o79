class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # okay so we will solve this by itteration


        answer = [[1]] # we know the first row is at least one

        # now that we have that we can start our loops

        for indexI in range(numRows - 1): # we subtract 1 because we already did the first row manually
            # okay now we should go to the last row

            tempForMath = [0] + answer[-1] + [0]
            # for example tempForMath will be [0][1][0]
            result = []

            for indexJ in range(len(tempForMath) - 1 ):
                # now add them
                result.append(tempForMath[indexJ] + tempForMath[indexJ + 1])
            
            # now that it has been added we append answer
            answer.append(result)
        
        return answer



