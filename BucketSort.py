from multiprocessing.heap import Heap
from typing import List
from HeapSort import HeapSort
from SortingAlgorithm import SortingAlgorithm

class BucketSort(SortingAlgorithm):
    def sort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        min_val, max_val = min(arr), max(arr)
        
        if min_val == max_val:
            return arr
        buckets = [[] for _ in range(n)]

        for val in arr:
            index = int((val - min_val) / (max_val - min_val) * (n - 1))
            buckets[index].append(val)

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(HeapSort().sort(bucket))

        return sorted_arr