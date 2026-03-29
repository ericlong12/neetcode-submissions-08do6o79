class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tempList = sorted(nums)
        answer = []
        
        for firstA in range(len(tempList)):
            if tempList[firstA] > 0:
                break  # No need to continue if first number is positive
            
            if firstA > 0 and tempList[firstA] == tempList[firstA - 1]:
                continue  # Skip duplicate firstA
            
            left = firstA + 1
            right = len(tempList) - 1
            
            while left < right:
                currSum = tempList[firstA] + tempList[left] + tempList[right]
                
                if currSum == 0:
                    answer.append([tempList[firstA], tempList[left], tempList[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate lefts
                    while left < right and tempList[left] == tempList[left - 1]:
                        left += 1
                    # Skip duplicate rights
                    while left < right and tempList[right] == tempList[right + 1]:
                        right -= 1
                        
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return answer
