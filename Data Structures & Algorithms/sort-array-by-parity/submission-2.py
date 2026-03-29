class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # we are given an array. move all even to front
        # move all odd the back

        # we can make a new array. 
        # if it is even, then add it to a seen set. 
        # then 2nd itteration. if it is not in seen. add it to seen

        # the brute force would be to pop

        # even = []
        # odd = []

        # for number in nums:
        #     if number % 2 == 0:
        #         even.append(number)
        #     else:
        #         odd.append(number)

        # return even + odd

        # okay lets solve this two pointers

        # so the left will keep on going. if it is odd
        # leave it there. if it is even, swap

        leftPointer = 0
        

        # now we loop the right

        for rightPointer in range(len(nums)):
            if nums[rightPointer] % 2 == 0:
                bucket = nums[leftPointer]
                nums[leftPointer] = nums[rightPointer]
                nums[rightPointer] = bucket
                leftPointer += 1
        return nums

















