import boto3
from boto3.dynamodb.conditions import Key
from os import getenv

region_name = getenv('APP_REGION')
todos_table = boto3.resource(
    'dynamodb', 
    region_name=region_name
 ).Table('Todos')

def lambda_handler(event, context):
    identity_id = 'developer:{}'.format(event['key'])
    response = todos_table.query(
        ExpressionAttributeNames={"#N":"Name"},
        KeyConditionExpression=Key('IdentityId').eq(identity_id),
        ProjectionExpression='Id, #N',
        Select='SPECIFIC_ATTRIBUTES'
    )
    todos = response['Items']
    return todos
