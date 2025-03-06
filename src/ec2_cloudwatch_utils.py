import boto3
from datetime import datetime, timedelta
import pandas as pd

# Initialize clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

# Get the last N instantiated instances
def get_last_n_instances(n):
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'LaunchTime': instance['LaunchTime']
            })
    instances.sort(key=lambda x: x['LaunchTime'], reverse=True)
    return [instance['InstanceId'] for instance in instances[:n]]

# Fetch CloudWatch metrics
def fetch_cloudwatch_metrics(instance_ids, metric_names, fetch_period):
    metrics = []
    id_to_meta = {}  # Maps ID to (metric_name, instance_id)

    for idx, instance_id in enumerate(instance_ids):
        for metric_name in metric_names:
            query_id = f"{metric_name.lower()}_{idx}"
            metrics.append({
                'Id': query_id,
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/EC2',
                        'MetricName': metric_name,
                        'Dimensions': [{'Name': 'InstanceId', 'Value': instance_id}]
                    },
                    'Period': 300,
                    'Stat': 'Average'
                }
            })
            id_to_meta[query_id] = (metric_name, instance_id)

    response = cloudwatch.get_metric_data(
        MetricDataQueries=metrics,
        StartTime=datetime.utcnow() - timedelta(hours=fetch_period),
        EndTime=datetime.utcnow(),
        ScanBy='TimestampAscending'
    )

    # Initialize metric_data structure
    metric_data = {metric: {instance: [] for instance in instance_ids} for metric in metric_names}

    for result in response['MetricDataResults']:
        query_id = result['Id']
        metric_name, instance_id = id_to_meta[query_id]
        for i, ts in enumerate(result['Timestamps']):
            metric_data[metric_name][instance_id].append({
                'Timestamp': ts,
                'Value': result['Values'][i]
            })

    # Convert to DataFrames
    final_metric_data = {}
    for metric in metric_names:
        dfs = []
        for instance in instance_ids:
            df = pd.DataFrame(metric_data[metric][instance])
            df = df.rename(columns={'Value': f'Node {instance_ids.index(instance)+1}'})
            dfs.append(df.set_index('Timestamp'))
        final_metric_data[metric] = pd.concat(dfs, axis=1).reset_index()

    return final_metric_data

