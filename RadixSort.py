from typing import List
from SortingAlgorithm import SortingAlgorithm

class RadixSort(SortingAlgorithm):
    def sort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        min_val = min(arr)
        if min_val < 0:
            arr = [x - min_val for x in arr]

        max_val = max(arr)
        
        exp = 1
        result = arr.copy()
        
        while max_val // exp > 0:
            result = self._counting_sort_by_digit(result, exp)
            exp *= 10
            
        if min_val < 0:
            result = [x + min_val for x in result]
            
        return result

    def _counting_sort_by_digit(self, arr: List[int], exp: int) -> List[int]:
        n = len(arr)
        output = [0] * n
        count = [0] * 10 

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        return output

if __name__ == '__main__':
    data = [10, 5, 12, 100, 90, 3, 119]
    print(RadixSort().sort(data))