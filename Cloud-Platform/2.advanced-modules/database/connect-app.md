# RDS 크레덴셜 저장하기
앞선 컴퓨트 실습에서 생성한 Web Server 인스턴스에는 RDS 사용을 위한 단순한 주소록을 생성하는 코드가 포함되어 있습니다. EC2 Web Server에서 RDS를 사용하기 위하여 아래의 실습을 진행합니다.

## RDS 크레덴셜 AWS Secrets Manager에 저장하기
구축한 웹 서버에는 주소록을 위한 샘플 코드가 포함되어 있습니다. 본 실습에서는 샘플 코드에 어떤 데이터 베이스를 사용할 것인지 그리고 어떻게 연결해야될지 명시하는 작업을 수행합니다. 해당 정보를 AWS Secrets Manager에 저장할 것입니다.

본 챕터에서 우리는 데이터 연결 정보를 포함한 secret을 생성할 것입니다. 추후, 우리는 웹 서버가 해당 secret를 불러올 수 있도록 적절한 권한을 부여할 것입니다.

1. 콘솔 창에서 [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/) 를 열고, Store a new secret 버튼을 클릭합니다.

![](../images/dev-secrets-manager-01.png)

2. Secret Type 아래, Credentials for Amazon RDS database를 선택합니다. 데이터 베이스를 생성할 때 입력했던 user name과 password를 적습니다. 그리고 Database 아래에 방금 생성한 데이터베이스를 선택합니다. 그리고 Next 버튼을 클릭합니다.

![](../images/gid-rds-15.png)

3. secret 이름을 mysecret으로 입력합니다. 샘플 코드에는 해당 이름의 secret을 묻도록 입력했기 때문에 해당 이름으로 입력해야 합니다. Next을 클릭합니다.

![](../images/dev-secrets-manager-04.png)

4. Secret rotation는 기본 값으로 두고 Next을 클릭합니다.

![](../images/dev-secrets-manager-05.png)

[Previous](./create-rds.md) | [Next](./update-asg.md)