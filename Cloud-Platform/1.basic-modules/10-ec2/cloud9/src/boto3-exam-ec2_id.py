# 설치 한 라이브러리를 사용할 수 있도록 가져 오기
import boto3

# AWS 리소스를 조작하는 준비 (클라이언트의 작성)
ec2_client = boto3.client ( 'ec2' )

# VPC 정보를 출력한다
#print (ec2_client.describe_vpcs ())

# EC2 정보를 출력한다
print (ec2_client.describe_instances ())