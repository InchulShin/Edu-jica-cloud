# 컴퓨트 – Amazon EC2

EC2[Amazon Elastic Compute Cloud(Amazon EC2)는 안전하고 크기 조정이 가능한 컴퓨팅 파워를 클라우드에서 제공하는 웹 서비스입니다. 개발자가 더 쉽게 웹 규모의 클라우드 컴퓨팅 작업을 할 수 있도록 설계되었습니다. Amazon EC2의 간단한 웹 서비스 인터페이스를 통해 간편하게 필요한 용량을 얻고 구성할 수 있습니다. 컴퓨팅 리소스에 대한 포괄적인 제어권을 제공하며, Amazon의 검증된 컴퓨팅 환경에서 실행할 수 있습니다.

## 목표 구성도
본 컴퓨트 실습은 앞서 네트워크 실습에서 생성한 VPC내 Private subnet들에 Auto Scaling Group을 이용하여 웹 서비스 인스턴스를 배포합니다. 이를 통해 고가용성이 보장되는 Web Service를 구성하여 외부 사용자가 Web Browser를 통하여 Sample Web Page에 접근할 수 있도록 구성합니다.

![](./images/gid-ec2-01.svg)

본 실습은 아래의 내용을 포함하고 있습니다.

- 웹 서버 인스턴스 시작(Launching) 및 사용자 지정 데이터(User Data)의 실행

- 보안 그룹(Security Group)의 설정

- 커스텀 AMI(Amazon Machine Image) 생성

- ALB(Application Load Balancer) 생성

- 시작 템플릿(Launch Template) 구성

- Auto Scaling Group 구성

- Auto Scaling 테스트 및 수동 설정 변경

## 실습 순서
이번 실습의 순서는 다음과 같습니다.

- 웹 서버 인스턴스의 시작

- 오토 스케일링 웹 서비스 배포

- 웹 서비스 확인 및 테스트

- 부록 - 추가적인 EC2 개념들

본 Lab Guide는 영어 AWS 관리 콘솔을 기준으로 작성되었습니다. EC2 Dashboard의 좌측 상단의 New EC2 Experience 탭이 활성화 상태인지 확인해 주십시오.

![](./images/gid-ec2-02.png)

[Previous](./network/30-index.md) | [Next](./compute/10-launching.md)