import boto3
from tabulate import tabulate

def get_ecs_services(cluster_name):
    ecs_client = boto3.client('ecs')
    services = []
    paginator = ecs_client.get_paginator('list_services')
    for page in paginator.paginate(cluster=cluster_name):
        services.extend(page['serviceArns'])
    return services

def get_service_details(cluster_name, service_arns):
    ecs_client = boto3.client('ecs')
    service_details = []
    for service_arn in service_arns:
        response = ecs_client.describe_services(
            cluster=cluster_name,
            services=[service_arn]
        )
        service = response['services'][0]
        task_definition = ecs_client.describe_task_definition(
            taskDefinition=service['taskDefinition']
        )
        task_def = task_definition['taskDefinition']

        service_details.append({
            'Service Name': service['serviceName'],
            'Number of Tasks': service['runningCount'],
            'CPU': task_def['cpu'],
            'Memory': task_def['memory']
        })
    return service_details

def main():
    cluster_name = 'your-cluster'  # Replace with your ECS cluster name
    services = get_ecs_services(cluster_name)
    service_details = get_service_details(cluster_name, services)

    # Print the table
    print(tabulate(service_details, headers="keys", tablefmt="pretty"))

if __name__ == "__main__":
    main()
