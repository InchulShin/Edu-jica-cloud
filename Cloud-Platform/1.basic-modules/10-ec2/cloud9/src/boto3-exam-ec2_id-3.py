# 설치 한 라이브러리를 사용할 수 있도록 가져 오기
import boto3
# AWS 리소스를 조작하는 준비 (클라이언트의 작성)

ec2_client = boto3.client ( 'ec2' )

# Describe 결과를 변수에 저장
ec2_data = ec2_client.describe_instances ()

# ec2_data ['Reservations']의 list를 하나씩 꺼내
for reservation in ec2_data ['Reservations'] :

    # reservation ['Instances']의 list를 하나씩 꺼내
    for instance in reservation ['Instances'] :

        # 위에서 추출 된 데이터의 인스턴스 ID를 출력한다
        print (instance ['InstanceId'])
