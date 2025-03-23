---

# ECS Service Details Script

This script retrieves and displays details of all services running under an AWS ECS cluster, including:
- Service Name
- Number of Tasks
- CPU Allocation
- Memory Allocation

The script uses the `boto3` library to interact with AWS and the `tabulate` library to format the output in a readable table.

---

## Prerequisites

Before running the script, ensure the following:

1. **AWS CLI Configuration**:
   - Install and configure the AWS CLI with your credentials:
     ```bash
     aws configure
     ```
   - Provide your AWS Access Key, Secret Key, Region, and default output format.

2. **Python Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install boto3 tabulate
     ```

---

## Script Details

### File: `ecs_service_details.py`

This script performs the following steps:
1. Retrieves all services in a specified ECS cluster.
2. Fetches details for each service, including:
   - Service Name
   - Number of Running Tasks
   - CPU Allocation
   - Memory Allocation
3. Displays the results in a formatted table.

---

## Usage

1. **Update the Cluster Name**:
   - Open the script and replace `'your-cluster-name'` with the name of your ECS cluster.

2. **Run the Script**:
   - Execute the script using Python:
     ```bash
     source myenv/bin/activate
     python ecs_service_details.py
     ```

3. **Output**:
   - The script will display a table with the details of all services in the cluster. Example:
     ```
     +-----------------+-----------------+-----+--------+
     |  Service Name   | Number of Tasks | CPU | Memory |
     +-----------------+-----------------+-----+--------+
     |  my-service-1   |
