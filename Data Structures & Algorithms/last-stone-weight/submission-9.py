import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # so we subtract the weight of the smaller stone
        # from the stone with greater weight

        # we continue until there is only one stone left

        # [2,3,6,2,4]
        # smash 6, 4
        # [2,3,2,2]
        # smash 3 and 2
        #[1,2,2]
        # smash 2 with 2
        # [1]


        # maxheap biggest nums on top

        # we take biggest 2 integers from maxHeap

        # we "smash"
        # we insert whatever is leftover back into the heap
        # heapify(heapname)
        # heappush(heapname, value)
        # heapq.heappop(stoneHeap)
        negativeStone = [-stone for stone in stones]

        heapq.heapify(negativeStone) 
        stoneHeap = negativeStone

        while len(stoneHeap) > 1:
            stone1 = heapq.heappop(stoneHeap)
            stone2 = heapq.heappop(stoneHeap)

            leftOverStone = -(abs(stone1 - stone2))
            
            if leftOverStone != 0:
                heapq.heappush(stoneHeap, leftOverStone)

        if not stoneHeap:
            return 0
        else:
            return -(stoneHeap[0])
            

        


