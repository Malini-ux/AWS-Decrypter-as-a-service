import boto3
import json
from boto3.dynamodb.conditions import Key,Attr
def lambda_handler(event, context):
        #shahHash = event['params']['path']['shaHash']
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('lookup')      
        path = event['path']
        extract = path.split('/')
        shahHash = extract[len(extract)-1]
        resp = table.get_item(Key={'key' : shahHash})
        if 'Item' in resp:
            return{'statusCode':200,'body':json.dumps({shahHash: resp['Item']['value']})}
        else:
            return{'statusCode':404,'body':"password is uncrackable"}