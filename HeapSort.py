import heapq
from SortingAlgorithm import *

class HeapSort(SortingAlgorithm):
    def sort(self, arr)-> List[int]:
        heapq.heapify(arr)
        sorted_arr = []
        while len(arr) > 0:
            sorted_arr.append(heapq.heappop(arr))
        return sorted_arr