import boto3

BUCKET = "onepic4emer"
KEY = "fire01.JPEG"

def detect_labels(bucket, key, max_labels=10, min_confidence=50, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']

def lambda_handler(event, context):
    # TODO implement
    for label in detect_labels(BUCKET, KEY):
        print "{Name} - {Confidence}%".format(**label)
    
