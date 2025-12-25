from datetime import datetime
import time
import tracemalloc
from typing import Dict, List, Optional, Tuple
from SortingAlgorithm import SortingAlgorithm
class SortBenchmarker:
    
    def __init__(self, all_data : List[List[int]]):
        self._all_data = all_data
    
    
    def _run_benchmark(self, sorting_algorithm : SortingAlgorithm, data)->Dict:
        tracemalloc.start()
        start_time = time.perf_counter()
        sorting_algorithm.sort(data.copy())
        _, memory_used = tracemalloc.get_traced_memory()
        time_used = (time.perf_counter() - start_time) * 1000
        tracemalloc.stop()
        return {"time_in_ms" : time_used, "memory_in_bytes" : memory_used}
    
    def run_benchmarks(self, sorting_algorithm : SortingAlgorithm)->Dict:
        total_time = 0
        total_memory = 0
        all_results = [self._run_benchmark(sorting_algorithm, data) for data in self._all_data]
        return {
            "time_in_ms" :  0 if len(self._all_data) == 0 else sum([result["time_in_ms"] for result in all_results]) / len(self._all_data),
            "memory_in_bytes" : 0 if len(self._all_data) == 0 else sum([result["memory_in_bytes"] for result in all_results]) / len(self._all_data),
        }
        
        
