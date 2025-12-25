import random
from CountSort import CountSort
from HeapSort import HeapSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from SortBenchmarker import SortBenchmarker
algorithms = [
    HeapSort(),
    QuickSort(),
    CountSort(),
]


for size in [100, 500, 1000, 500000]:
    data = [random.randint(0, 1000) for _ in range(size)]
    benchmarker = SortBenchmarker(data)
    for algo in algorithms:
        print(algo.name, size, benchmarker.run_benchmark(algo))