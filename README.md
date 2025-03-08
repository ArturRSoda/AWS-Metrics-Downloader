# AWS Metrics Downloader

This Python script fetches CloudWatch metrics for the most recent EC2 instances, organizes the data into CSV files, and generates line graphs for visualization.

## Features
- Fetches metrics like `CPUUtilization`, `CPUCreditUsage`, `CPUCreditBalance`, etc.
- Saves metrics to CSV files (one file per metric).
- Generates line graphs for each metric (one graph per metric).
- Handles missing or incomplete data gracefully.
- Configurable via a `config.yaml` file.

## Pre-requisites

Before running the script, ensure you have the following:

1. **Python 3.8+**: The script is written in Python and requires Python 3.8 or later.
2. **Boto3**: The AWS SDK for Python.
3. **Pandas**: For data manipulation and CSV export.
4. **Matplotlib**: For generating line graphs.
5. **PyYAML**: For reading the `config.yaml` file.
6. **AWS CLI**: For configuring AWS credentials.
   - Configure credentials: `aws configure`

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/aws-metrics-downloader.git
   cd aws-metrics-downloader
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
    - Provide your AWS Access Key, Secret Key, region, and output format.

   ```bash
   aws configure
   ```

4. Modify the `config.yaml` file:
    - Open `config.yaml` and update the configuration as needed.

## Usage

Run the script with the following command:

   ```bash
   python3 main.py
   ```

###output

- **CSV Files**: Saved in the `csv_dir` directory.
- **Graphs**: Saved in the `graph_dir` directory.

