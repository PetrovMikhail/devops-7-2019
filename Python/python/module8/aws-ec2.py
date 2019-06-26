from typing import List

import boto3

client = boto3.client('ec2')

availability_zone = "us-east-1a"
current_status = "stopped"
assigned_command = "start"


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
    if command == "start":
        start_instances(filtered_instances)
    elif command == "stop":
        stop_instances(filtered_instances)
    elif command == "reboot":
        reboot_instances(filtered_instances)
    elif command == "terminate":
        terminate_instances(filtered_instances)
    else:
        print("Chosen command is not supported by aws ec2 console")


def start_instances(list_id: List):
    client.start_instances(InstanceIds=list_id)
    for instance_id in list_id:
        print("Instance {} is successfully started".format(instance_id))


def stop_instances(list_id: List):
    client.stop_instances(InstanceIds=list_id)
    for instance_id in list_id:
        print("Instance {} is successfully stopped".format(instance_id))


def reboot_instances(list_id: List):
    client.reboot_instances(InstanceIds=list_id)
    for instance_id in list_id:
        print("Instance {} is successfully rebooted".format(instance_id))


def terminate_instances(list_id: List):
    client.terminate_instances(InstanceIds=list_id)
    for instance_id in list_id:
        print("Instance {} is successfully terminated".format(instance_id))


if __name__ == "__main__":
    change_status(region=availability_zone, status=current_status, command=assigned_command)
