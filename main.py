from src.ec2_cloudwatch_utils import get_last_n_instances, fetch_cloudwatch_metrics
from src.files_generator import save_metrics_to_files, generate_line_graphs
from src.config_reader import config_reader

def main():
    config = config_reader()
    n_instances = config[0]
    fetch_period = config[1]
    csv_dir = config[2]
    graph_dir = config[3]
    metric_names = config[4]

    instance_ids = get_last_n_instances(n_instances)
    metric_data = fetch_cloudwatch_metrics(instance_ids, metric_names, fetch_period)
    save_metrics_to_files(metric_data, csv_dir)
    generate_line_graphs(csv_dir, graph_dir)

if __name__ == '__main__':
    main()
