import yaml

def config_reader():
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

        return (
            data["n_instances"],
            data["fetch_period"],
            data["csv_dir"],
            data["graph_dir"],
            data["graph_title"],
            data["metrics_to_fetch"]
        )


