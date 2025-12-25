from SortingAlgorithm import *
import random

class QuickSort(SortingAlgorithm):
    def sort(self,arr) -> list[int]:
        if len(arr) <= 1:
            return arr
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.sort(left) + middle + self.sort(right)
