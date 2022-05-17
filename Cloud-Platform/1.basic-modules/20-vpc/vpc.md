# VPC 실습

## Amazon VPC(Virtual Private Cloud) 에 대해서
[Amazon Virtual Private Cloud(Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) 를 이용하면 사용자가 정의한 가상 네트워크로 AWS 리소스를 시작할 수 있습니다. 이 가상 네트워크는 AWS의 확장 가능한 인프라를 사용한다는 이점과 함께 고객의 자체 데이터 센터에서 운영하는 기존 네트워크와 매우 유사합니다.

Amazon VPC를 사용하면 사용자가 정의하는 논리적으로 격리된 가상 네트워크에서 AWS 리소스를 시작할 수 있습니다. IP 주소 범위 선택, 서브넷 생성, 라우팅 테이블 및 네트워크 게이트웨이 구성 등 가상 네트워킹 환경을 완벽하게 제어할 수 있습니다. 리소스 및 애플리케이션에 대한 안전하고 쉬운 액세스를 보장하도록 지원하기 위해 IPv4 및 IPv6를 가상 사설 클라우드 내 대개의 리소스에 대해 사용할 수 있습니다.

![](../images/amazon-vpc-architecture.svg)

아래의 순서 대로 실습을 진행하면서 네트워크를 직접 구성합니다:

- VPC 생성하기

- 추가 서브넷 생성하기

- 라우팅 테이블 편집하기

- 보안 그룹 생성하기

- 실습 자원 삭제

[Previous](../20-vpc.md) | [Next](../vpc/1-vpc.md)