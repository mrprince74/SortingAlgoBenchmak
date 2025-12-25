from SortingAlgorithm import *

class MergeSort(SortingAlgorithm):
    def sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        
        left_half = self.sort(arr[:mid])
        right_half = self.sort(arr[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list