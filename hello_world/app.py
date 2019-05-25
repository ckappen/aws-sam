import json
import boto3
import botostubs
from botocore.vendored import requests

ec2 = boto3.client('ec2')   # type: botostubs


def fetchEC2(filters):
    response = ec2.describe_instances(Filters=filters)
    return response


def lambda_handler(event, context):

    response = fetchEC2([
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        },
        {
            'Name': 'tag:aws:autoscaling:groupName',
            'Values': ['testing-servers-group']
        }
    ])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            print(instance_id)
#            ec2.filterterminate_instances(instance_ids=)

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }
