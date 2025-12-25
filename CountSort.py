from collections import defaultdict
from SortingAlgorithm import *

class CountSort(SortingAlgorithm):
    def sort(self, arr)->List[int]:
        min_num = min(arr)
        max_num = max(arr)
        hash_table = defaultdict(int)
        for num in arr:
            hash_table[num]+= 1
        
        sorted_arr = []
        for num in range(min_num, max_num + 1):
            if num in hash_table:
                sorted_arr.extend([num * hash_table[num]])
        return sorted_arr