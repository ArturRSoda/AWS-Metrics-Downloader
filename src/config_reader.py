import yaml

def config_reader():
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

        metrics = [list(metric.keys())[0] for metric in data["metrics_to_fetch"]]
        graph_titles = [list(metric.values())[0]["graph_title"] for metric in data["metrics_to_fetch"]]

        return (
            data["n_instances"],
            data["fetch_period"],
            data["csv_dir"],
            data["graph_dir"],
            metrics,
            graph_titles
        )


