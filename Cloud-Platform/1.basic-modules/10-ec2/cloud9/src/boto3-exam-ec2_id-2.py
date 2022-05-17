import boto3

# AWS 리소스를 조작하는 준비 (클라이언트의 작성)
ec2_client = boto3.client ( 'ec2' )

# VPC 정보를 출력한다
print (ec2_client.describe_vpcs ())

# 인스턴스 ID를 출력한다
print (ec2_client.describe_instances ()['Reservations'][0]['Instances'][0]['InstanceId'])
