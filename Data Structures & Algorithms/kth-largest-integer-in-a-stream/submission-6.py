import heapq

class KthLargest:
    # the stream is not sorted
    # we have to find the kth largest element
    # these elements do not have to be unique

    # heaps are useful for finding the kth largest

    # min or max heap?
    # we use min heap of size len(k)

    # minHeap[0] 
    # this is how we access the smallest element

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.target = k


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        heapq.heapify(self.minHeap)

        while len(self.minHeap) >= self.target:
            popped = heapq.heappop(self.minHeap)
        heapq.heappush(self.minHeap,popped)
        return popped


        









