# 실습 자원 삭제하기

## 실습 자원 삭제하기
[EC2 콘솔](https://console.aws.amazon.com/ec2/v2/home?#Instances:) 에서 dev-instance와 prod-instance를 삭제합니다.

![](../../images/iam-5-01.png)

[IAM 콘솔](https://console.aws.amazon.com/iam/home?region=us-west-2#/home) 에서 생성한 모든 IAM Identities를 삭제합니다.

- User groups: dev-group

![](../../images/iam-5-02.png)

- Users: dev-user

![](../../images/iam-5-03.png)

- Roles: IAMBucketTestRole

![](../../images/iam-5-04.png)

Policies: DevPolicy, IAMBucketTestPolicy

![](../../images/iam-5-05.png)

[S3 콘솔](https://s3.console.aws.amazon.com/s3) 에서 iam-test-사용자 이름과 iam-test-other-사용자 이름 버킷을 삭제합니다. iam-test-사용자 이름을 삭제하기 이전 버킷 Empty 작업을 먼저 수행합니다.

![](../../images/iam-5-06.png)

![](../../images/iam-5-07.png)

[Previous](./4-iam.md) | [Next](../../40-monitoring.md)