import json
import boto3
import botostubs

ec2 = boto3.resource('ec2')   # type: botostubs


def terminate(filters):
    print(filters)
    response = ec2.instances.filter(Filters=filters)
    terminated_instance_ids = []
    for instance in response:
        # ec2.instances.filter(InstanceIds=[instance.id]).terminate()
        terminated_instance_ids.append(instance.id)

    return terminated_instance_ids


def lambda_handler(event, context):
    filters = [
        {
            "Name": "state",
            "Values": ["available"]
        }
    ]

    response = ec2.describe_images(
        Owners=["self"],
        Filters=filters
    )
    print(response)
    # terminated_instance_ids = terminate(event["filters"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "terminated_instance_ids": deregister_ami_ids
        }),
    }
    pass
