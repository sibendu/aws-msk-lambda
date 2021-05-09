import json
#import boto3
import base64

def lambda_handler(event, context):  
  
    print(event)
    records = event['records']
    orders = records['orders-0']
    thisOrder =  orders[0]
    msg = thisOrder['value']
    msg = base64.b64decode(msg).decode('utf-8')    
    print(msg)
        
    return {
        'statusCode': 200,
        'body': msg
    }