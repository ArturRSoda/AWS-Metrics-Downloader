import os
import pandas as pd
import matplotlib.pyplot as plt
from PyPDF2 import PdfMerger

# Save metrics to CSV files
def save_metrics_to_files(metric_data, output_dir='metrics'):
    if (not os.path.exists(output_dir)):
        os.makedirs(output_dir)

    for metric, df in metric_data.items():
        df.to_csv("%s/%s.csv" % (output_dir, metric), index=False)
        print("CSV file for metric %s generated successfully!" % metric)
    print()

#  Generate graphs
def generate_line_graphs(output_dir='metrics', graph_dir='graphs', title=None):
    print(title)
    if (not os.path.exists(graph_dir)):
        os.makedirs(graph_dir)

    colors = plt.cm.tab20.colors  # 20 distinct colors

    for csv_file in os.listdir(output_dir):
        if (csv_file.endswith('.csv')):
            metric_name = csv_file.split('.')[0]
            df = pd.read_csv("%s/%s" % (output_dir, csv_file))

            # Convert to datetime and extract time
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df['Time'] = df['Timestamp'].dt.strftime('%H:%M:%S')

            plt.figure(figsize=(12, 6))

            # Plot each node with time-formatted x-axis
            for i, col in enumerate(df.columns[1:-1]):  # Skip Timestamp and Time columns
                plt.plot(df['Time'], df[col], color=colors[i], label= "Node %d" % (i+1))

            # Format x-axis
            plt.xticks(rotation=45)
            plt.xlabel('Time (HH:MM:SS)')
            plt.ylabel('Value')
            plt.title("%s Over TIme" % (metric_name) if (title==None) else title)
            plt.legend(bbox_to_anchor=(1.05, 1))
            plt.tight_layout()

            plt.savefig("%s/%s.pdf" % (graph_dir, metric_name))
            plt.close()

            print("Graph for file %s generated successfully!" % (csv_file))

    print()
    pdf_merger(graph_dir)
    print("All pdfs merged successfully!")
    print()


def pdf_merger(graph_dir='graphs'):
    files = [file for file in os.listdir(graph_dir) if (file.endswith('.pdf'))]

    merger = PdfMerger()

    for pdf in files:
        merger.append(open(graph_dir+"/"+pdf, 'rb'))

    with open(graph_dir+"/AllGraphs.pdf", "wb") as result:
        merger.write(result)


