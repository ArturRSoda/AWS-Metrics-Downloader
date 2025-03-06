import os
import pandas as pd
import matplotlib.pyplot as plt

# Save metrics to CSV files
def save_metrics_to_files(metric_data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for metric, df in metric_data.items():
        df.to_csv(f"{output_dir}/{metric.lower()}.csv", index=False)

#  Generate graphs
def generate_line_graphs(output_dir='metrics', graph_dir='graphs'):
    if not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    colors = plt.cm.tab20.colors  # 20 distinct colors

    for csv_file in os.listdir(output_dir):
        if csv_file.endswith('.csv'):
            metric_name = csv_file.split('.')[0]
            df = pd.read_csv(f"{output_dir}/{csv_file}")

            # Convert to datetime and extract time
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df['Time'] = df['Timestamp'].dt.strftime('%H:%M:%S')

            plt.figure(figsize=(12, 6))

            # Plot each node with time-formatted x-axis
            for i, col in enumerate(df.columns[1:-1]):  # Skip Timestamp and Time columns
                plt.plot(df['Time'], df[col], color=colors[i], label=f'Node {i+1}')

            # Format x-axis
            plt.xticks(rotation=45)
            plt.xlabel('Time (HH:MM:SS)')
            plt.ylabel('Value')
            plt.title(f"{metric_name} Over Time")
            plt.legend(bbox_to_anchor=(1.05, 1))
            plt.tight_layout()

            plt.savefig(f"{graph_dir}/{metric_name}.pdf")
            plt.close()
