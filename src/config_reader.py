import json

def config_reader():
    f = open('configs.json')
    data = json.load(f)
    return (
        data["n_instances"],
        data["fetch_period"],
        data["csv_dir"],
        data["graph_dir"],
        data["metrics_to_fetch"]
    )

