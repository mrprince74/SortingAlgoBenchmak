import random
from BucketSort import BucketSort
from CountSort import CountSort
from Exporter import Exporter
from HeapSort import HeapSort
from QuickSort import QuickSort
from RadixSort import RadixSort
from SortBenchmarker import SortBenchmarker
from TestCaseGenerator import TestCaseGenerator
from Visualizer import Visualizer
from pprint import pprint
SET_SIZE = 10
def main():
    algorithms = [
        HeapSort(),
        QuickSort(),
        CountSort(),
        BucketSort(),
        RadixSort(),
    ]
    test_sets = {
        "Small Set" : [TestCaseGenerator.generate_small() for _ in range(SET_SIZE)],
        "Medium Set" : [TestCaseGenerator.generate_medium() for _ in range(SET_SIZE)],
        "Large Set" : [TestCaseGenerator.generate_large() for _ in range(SET_SIZE)],
        "Already Sorted Set" : [TestCaseGenerator.generate_already_sorted() for _ in range(SET_SIZE)],
        "Reverse Sorted Set" : [TestCaseGenerator.generate_reverse_sorted() for _ in range(SET_SIZE)],
        "Identical Set" : [TestCaseGenerator.generate_identical() for _ in range(SET_SIZE)],
    }

    benchmarker_data = {}
    for set_name, data  in test_sets.items():
        benchmarker = SortBenchmarker(data)
        benchmarker_data[set_name] = {}
        for algo in algorithms:
            data = benchmarker.run_benchmarks(algo)
            benchmarker_data[set_name][algo.name] = data
        
    pprint(benchmarker_data)
    Exporter.export_to_excel(benchmarker_data)
    Visualizer.draw_benchmarks(benchmarker_data)


if __name__ == '__main__':
    main()