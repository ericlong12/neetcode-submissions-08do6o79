class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # we multiply all the number together.
        # now we divide the total by our current number

        # we append that to the list

        # the testcase we fail is that we don't return negative number


        total = 1

        for number in nums:
            total = number * total
        
        answer = []
        for index in range(len(nums)) :
            if nums[index] == 0:
                leftTotal = 1
                rightTotal = 1
                for num1 in nums[0:index]:
                    leftTotal *= num1
                for num2 in nums[index+1:len(nums)]:
                    rightTotal *= num2
                answer.append(leftTotal*rightTotal)
            else:
                answer.append(int((total / nums[index])))

        return answer

