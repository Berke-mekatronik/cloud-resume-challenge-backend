import json
import boto3
import os


TABLE_NAME = os.environ.get("TABLE_NAME", "VisitorCounter")

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME) # Table name must be exact same

def lambda_handler(event, context):
    # Get current count
    response = table.get_item(Key={
        'visitor_count_id': 0
        })
    # Convert Decimal to int
    visitor_count = int(response['Item'].get('visitor_count', 0))  
    # Increase count
    visitor_count += 1

    # Write the new count into the table
    table.put_item(Item={
        'visitor_count_id': 0,
        'visitor_count': visitor_count
    })

    # Return valid JSON response
    # It is necessary to avoid CORS errors. If it is missing, the browser will block the fetch.
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': visitor_count})
    }
