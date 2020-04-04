import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')
todos_table = boto3.resource(
    'dynamodb', 
    region_name=region_name
 ).Table('Todos')

def lambda_handler(event, context):
    identity_id = 'developer:{}'.format(event['key'])
    name = event['Name']
    id = str(uuid4())
    todos_table.put_item(Item={
        'IdentityId': identity_id,
        'Id': id,
        'Name': name,
    })
    return {
        'Id': id,
        'Name': name,
    }
