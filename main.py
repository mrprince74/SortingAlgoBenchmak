import random
from CountSort import CountSort
from HeapSort import HeapSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from SortBenchmarker import SortBenchmarker
from Visualizer import Visualizer
from pprint import pprint

def main():
    algorithms = [
        HeapSort(),
        QuickSort(),
        CountSort(),
    ]



    benchmarker_data = {}
    for size in [100, 500, 1000]:
        data = [random.randint(0, 1000) for _ in range(size)]
        benchmarker = SortBenchmarker(data)
        benchmarker_data[size] = {}
        for algo in algorithms:
            data = benchmarker.run_benchmark(algo)
            benchmarker_data[size][algo.name] = data
            metrics = list(data.keys())

    pprint(benchmarker_data)
    Visualizer.draw_benchmarks(benchmarker_data)


if __name__ == '__main__':
    main()