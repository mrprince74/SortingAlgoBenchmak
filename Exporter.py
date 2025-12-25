import pandas as pd

class Exporter:
    @staticmethod
    def export_to_excel(results: dict, filename: str = "Results/benchmark_results.xlsx"):
        # Flatten the nested dictionary into a list of rows
        data_rows = []
        
        for test_set, algos in results.items():
            for algo_name, metrics in algos.items():
                row = {
                    "Test Set": test_set,
                    "Algorithm": algo_name,
                    "Time (ms)": metrics.get("time_in_ms"),
                    "Memory (Bytes)": metrics.get("memory_in_bytes")
                }
                data_rows.append(row)
        
        # Create a DataFrame
        df = pd.DataFrame(data_rows)
        
        # Create an Excel writer object to allow for some basic formatting
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Performance Data')
            
            # Auto-adjust column widths for readability
            worksheet = writer.sheets['Performance Data']
            for idx, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.column_dimensions[chr(65 + idx)].width = max_len

        print(f"Successfully exported results to {filename}")