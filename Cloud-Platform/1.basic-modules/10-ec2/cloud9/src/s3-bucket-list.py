import boto3

client = boto3.client('s3')

response = client.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

print("Bucket List: %s" % buckets)
