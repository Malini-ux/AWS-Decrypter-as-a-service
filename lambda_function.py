import boto3
import json
from boto3.dynamodb.conditions import Key,Attr
def lambda_handler(event, context):
        shahHash = event['params']['path']['shaHash']
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('lookup')      
        resp = table.query(KeyConditionExpression=Key('key').eq(shahHash))
        count = resp['Count']
        if count == 0: 
          statusCode=404
          return {'error':"Unable to crack password"}
        else:
          password = resp['Items'][0]
          hash =password['key']
          password = password['value']
          statusCode=200
          return {hash : password}