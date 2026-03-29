class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # we are given an array. move all even to front
        # move all odd the back

        # we can make a new array. 
        # if it is even, then add it to a seen set. 
        # then 2nd itteration. if it is not in seen. add it to seen

        # the brute force would be to pop

        even = []
        odd = []

        for number in nums:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        even.extend(odd)

        return even