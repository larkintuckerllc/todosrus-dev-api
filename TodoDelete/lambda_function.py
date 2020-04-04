import boto3
from boto3.dynamodb.conditions import Attr, Key
from os import getenv

region_name = getenv('APP_REGION')
todos_table = boto3.resource(
    'dynamodb', 
    region_name=region_name
 ).Table('Todos')

def lambda_handler(event, context):
    identity_id = 'developer:{}'.format(event['key'])
    id = event['Id']
    key = {
        'IdentityId': identity_id,
        'Id': id,
    }
    todos_table.delete_item(
        ConditionExpression=Attr('IdentityId').eq(identity_id) & Attr('Id').eq(id),
        Key=key
    )
    return {
        'Id': id,
    }
