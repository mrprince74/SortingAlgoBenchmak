from typing import List
import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    @staticmethod
    def draw_benchmarks(results: dict):
        test_sets = list(results.keys())
        if not test_sets:
            return
            
        algos = list(results[test_sets[0]].keys())
        
        # Updated to match your Benchmarker return keys
        metrics = ['time_in_ms', 'memory_in_bytes']
        titles = ['Execution Time', 'Peak Memory Usage']
        ylabels = ['Milliseconds (ms)', 'Bytes']
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        x = np.arange(len(test_sets))
        bar_width = 0.8 / len(algos)
        
        for i, metric in enumerate(metrics):
            ax = axes[i]
            for j, algo in enumerate(algos):
                # Extract values using the specific keys from your Benchmarker
                values = [results[ts].get(algo, {}).get(metric, 0) for ts in test_sets]
                offset = (j - (len(algos) - 1) / 2) * bar_width
                ax.bar(x + offset, values, bar_width, label=algo)
            
            ax.set_title(titles[i], fontweight='bold')
            ax.set_ylabel(ylabels[i])
            ax.set_xticks(x)
            ax.set_xticklabels(test_sets)
            ax.legend()
            ax.grid(axis='y', linestyle='--', alpha=0.6)

        plt.tight_layout()
        plt.show()