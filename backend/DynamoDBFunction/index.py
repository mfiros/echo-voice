import json
import boto3
import os
from aws_lambda_powertools import Logger, Tracer
from botocore.exceptions import ClientError


logger = Logger()
tracer = Tracer()
dynamodb = boto3.resource('dynamodb')
dynamodb_table = os.environ.get('TABLE_NAME')
table = dynamodb.Table(dynamodb_table)

# this function is used by frontend to query dynamodb and get details of last 5 calls


def get_last_5_items():
    response = table.scan(
        Limit=5,
        Select='ALL_ATTRIBUTES'  # Retrieve all attributes of the items
    )
    items = response['Items']
    while 'LastEvaluatedKey' in response:
        last_key = response['LastEvaluatedKey']
        response = table.scan(
            Limit=10,
            ExclusiveStartKey=last_key,
            Select='ALL_ATTRIBUTES'  # Retrieve all attributes of the items
        )
        items.extend(response['Items'])
    items_sorted = sorted(items, key=lambda x: x['calledOn'], reverse=True)
    transformed_items = []
    for item in items_sorted:
        transformed_item = {
            'callerNumber': item['callerNumber'],
            'result': item['result'],
            'lastcalled': int(item['calledOn'])
        }
        transformed_items.append(transformed_item)
    return transformed_items


def lambda_handler(event, context):
    """
    Lambda handler.
    Args:
        event (dict): A dictionary representing the event that triggered
            this function.
        context (object): An object representing the runtime context in
            which this function is running.
    Returns:
        dict: A dictionary containing the response.
    """
    logger.info(event)
    # print(event)

    res = get_last_5_items()
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps(res[:5])
    }
