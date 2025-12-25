from datetime import datetime
from time import time
import tracemalloc
from typing import Dict, List, Optional, Tuple
from SortingAlgorithm import SortingAlgorithm

class SortBenchmarker:
    
    def __init__(self, data : List[int]):
        self._data = data
    
    def run_benchmark(self, sorting_algorithm : SortingAlgorithm)->Dict:
        tracemalloc.start()
        start_time = datetime.now()
        sorted = sorting_algorithm.sort(self._data.copy())
        _, memory_used = tracemalloc.get_traced_memory()
        time_used = (datetime.now() - start_time).microseconds / 1000
        tracemalloc.stop()
        return {"time_in_ms" : time_used, "memory_in_bytes" : memory_used}
