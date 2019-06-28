from typing import List

import boto3

client = boto3.client('ec2')

availability_zone = "us-east-1a"
current_status = "running"
assigned_command = "stop"


def collect_instances(region: str, status: str) -> List:
    instances = []
    response = client.describe_instances(Filters=[{'Name': 'availability-zone', 'Values': [region]},
                                                  {'Name': 'instance-state-name', 'Values': [status]}])
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(instance["InstanceId"])
    return instances


def change_status(region: str, status: str, command: str) -> None:
    filtered_instances = collect_instances(region, status)
    for instance in filtered_instances:
        try:
            instance_method = getattr(client, '{}_instances'.format(command))
            instance_method(InstanceIds=[instance])
            print("Instance {} is successfully {}".format(instance, command))
        except:
            print("Chosen command is not supported by aws ec2 console")


if __name__ == "__main__":
    change_status(region=availability_zone, status=current_status, command=assigned_command)
