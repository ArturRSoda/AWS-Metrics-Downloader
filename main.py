from src.ec2_cloudwatch_utils import get_last_n_instances, fetch_cloudwatch_metrics
from src.files_generator import save_metrics_to_files, generate_line_graphs
from src.config_reader import config_reader

def main():
    n_instances, fetch_period, csv_dir, graph_dir, graph_title, metric_names = config_reader()

    instance_ids = get_last_n_instances(n_instances)
    metric_data = fetch_cloudwatch_metrics(instance_ids, metric_names, fetch_period)
    save_metrics_to_files(metric_data, csv_dir)
    generate_line_graphs(csv_dir, graph_dir, graph_title)

    print("Files generated successfully!")

if __name__ == '__main__':
    main()
