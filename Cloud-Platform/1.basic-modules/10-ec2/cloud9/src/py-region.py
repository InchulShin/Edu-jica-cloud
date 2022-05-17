import boto3

client = boto3.client('ec2')
region = map(lambda x: x['RegionName'], ec2.describe_regions()['Regions'])

for region in regions:
	print(region)
	client = boto3.client('ec2', region_name=region)