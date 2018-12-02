import json
import urllib
import boto3
import time
import logging
import os
import requests
#from botocore.vendored import requests
from datetime import datetime

def detect_labels( max_labels=10, min_confidence=50, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	headers ={'Content-Type': 'application/json','Authorization': 'Bearer 9JxmzOjA8c41FejOXkG708mK7fjFR6NQPCYOGfzrg3hAUbKpsULDkj4TLTF+R1m5si/AXQVx1RrwvjktI+jkSFV6ii+ERsobrWr8fvSuOshgCi61zuthnzVUjdOxBy/kk+oOLZd2C/0FSDXCRz8lFQdB04t89/1O/w1cDnyilFU='}
	response = requests.get('https://api.line.me/v2/bot/message/8945907941044/content',headers=headers)
	response_context = response.content
	response = rekognition.detect_labels(
		Image={'Bytes':  response_context }
	)
	print response['Labels'][0]['Name']
	return response['Labels']

def lambda_handler(event, context):
    # TODO implement
    #BUCKET = event['Records'][0]['s3']['bucket']['name']
    #KEY = event['Records'][0]['s3']['object']['key']
    #print event['Records'][0]
    #dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    #table = dynamodb.Table('alertmessage')
    #detect_labels()
    '''
    for label in detect_labels(BUCKET, KEY):
    	#print "{Name} - {Confidence}%".format(**label)
    	print label['Name']
    	response = table.put_item(Item={'word':label['Name'],'location':"kbtg"})
    '''
    message = {"name": "fire"
        ,"location":"kbtg"
    }
    client = boto3.client('sns')
    response = client.publish(
    	TargetArn='arn:aws:sns:us-east-1:590113514737:alert',
    	Message=json.dumps({'default': json.dumps(message)}),
    	MessageStructure='json'
    )
    