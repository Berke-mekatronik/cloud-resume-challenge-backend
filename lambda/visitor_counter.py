import json
import os
import boto3

def get_table():
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.environ.get("AWS_REGION", "eu-central-1")
    )
    return dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    table = get_table()

    response = table.get_item(
        Key={"visitor_count_id": 0}
    )

    visitor_count = int(response.get("Item", {}).get("visitor_count", 0))
    visitor_count += 1

    table.put_item(
        Item={
            "visitor_count_id": 0,
            "visitor_count": visitor_count
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"count": visitor_count})
    }
