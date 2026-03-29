class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1, always has the empty spots at the end
        # nums2, will be merged into nums1

        # we have 3 pointers, when the far left is out of index
        # then we should append the rest

        # we do this because it is 0 indexed
        # we compare this pointer to the other pointer on the other array
        # it could go out of index
        leftPointer = m - 1

        # we make the right pointer
        # this pointer will change the values all the time
        rightPointer = len(nums1) - 1

        # now we make the other pointer for the nums2
        endOfNums2 = len(nums2) - 1

        while endOfNums2 >= 0 and leftPointer >= 0:
            if nums2[endOfNums2] >= nums1[leftPointer]:
                nums1[rightPointer] = nums2[endOfNums2]
                endOfNums2 -= 1

            elif nums2[endOfNums2] < nums1[leftPointer]:
                nums1[rightPointer] = nums1[leftPointer]
                leftPointer -= 1
            rightPointer -= 1

        while endOfNums2 >= 0:
            nums1[rightPointer] = nums2[endOfNums2]
            rightPointer -= 1
            endOfNums2 -= 1

        
        





