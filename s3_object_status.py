import boto3

REGION='eu-west-1'
BUCKET='uploadtmphires'
PREFIX='hires'
FILENAME=PREFIX+'/'+'AWTF1R.jpg'

conn = boto3.client("s3", REGION)

file_ver = conn.head_object(Bucket=BUCKET, Key=FILENAME)
print(file_ver['ResponseMetadata']['HTTPStatusCode'])
