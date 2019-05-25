import json
import boto3
import botostubs

ec2 = boto3.resource('ec2')   # type: botostubs


def lambda_handler(event, context):

    instances = ec2.instances.filter(Filters=event["filters"])

    terminated_instance_ids = []
    for instance in instances:
        # ec2.instances.filter(InstanceIds=[instance.id]).terminate()
        terminated_instance_ids.append(instance.id)

    print(terminated_instance_ids)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "terminated_instance_ids": terminated_instance_ids
        }),
    }
