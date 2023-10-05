import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student')  # Replace with your table name

def create(event, context):
    # Create a new item in the DynamoDB table
    body = json.loads(event['body'])
    response = table.put_item(Item=body)
    return {
        'statusCode': 200,
        'body': json.dumps('Item created successfully')
    }

def read(event, context):
    # Read an item from the DynamoDB table
    item_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': item_id})
    item = response.get('Item')
    
    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps('Item not found')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def update(event, context):
    # Update an item in the DynamoDB table
    item_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    response = table.update_item(
        Key={'id': item_id},
        UpdateExpression='SET #data = :data',
        ExpressionAttributeNames={'#data': 'data'},
        ExpressionAttributeValues={':data': body['data']}
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Item updated successfully')
    }

def delete(event, context):
    # Delete an item from the DynamoDB table
    item_id = event['pathParameters']['id']
    response = table.delete_item(Key={'id': item_id})
    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
    }
