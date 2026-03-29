class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solve this like two sum part 2 with 2 pointers
        # make sure you don't hit the edge case and you will be good

        nums.sort()
        answer = []

        for index, number in enumerate(nums):
            # if the left most number is greater than one
            # This means that we cannot solve the problem
            if number > 0:
                # we choose to exit the loop here, its over:
                break
            
            # this is done to make sure that there is no duplicates
            if index > 0 and nums[index] == nums[index-1]:
                continue
            # the left pointer should be always to the right of index
            left = index + 1
            right = len(nums) - 1

            # when the left and right pointer touch, then we are done
            while left < right:
                if nums[left] + nums[right] + nums[index] == 0:
                    answer.append([nums[left], nums[right], number])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

                elif nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
        return answer
                
                










