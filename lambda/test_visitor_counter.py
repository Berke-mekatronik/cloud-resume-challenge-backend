import json
import os
import boto3
import pytest
from moto import mock_dynamodb

# Import AFTER mocking
@mock_dynamodb
def test_lambda_increments_visitor_count():
    # Arrange
    os.environ["TABLE_NAME"] = "VisitorCounter"

    dynamodb = boto3.resource("dynamodb", region_name="eu-central-1")

    table = dynamodb.create_table(
        TableName="VisitorCounter",
        KeySchema=[
            {"AttributeName": "visitor_count_id", "KeyType": "HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "visitor_count_id", "AttributeType": "N"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    # Seed initial item
    table.put_item(
        Item={
            "visitor_count_id": 0,
            "visitor_count": 5
        }
    )

    # Import lambda AFTER table exists
    from visitor_counter import lambda_handler

    # Act
    response = lambda_handler({}, {})

    body = json.loads(response["body"])

    # Assert
    assert response["statusCode"] == 200
    assert body["count"] == 6

@mock_dynamodb
def test_lambda_creates_initial_counter():
    os.environ["TABLE_NAME"] = "VisitorCounter"

    dynamodb = boto3.resource("dynamodb", region_name="eu-central-1")

    dynamodb.create_table(
        TableName="VisitorCounter",
        KeySchema=[
            {"AttributeName": "visitor_count_id", "KeyType": "HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "visitor_count_id", "AttributeType": "N"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    from visitor_counter import lambda_handler

    response = lambda_handler({}, {})
    body = json.loads(response["body"])

    assert body["count"] == 1
