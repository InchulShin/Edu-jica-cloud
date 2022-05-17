# EC2 Windows 실습

## Amazon EC2에 대하여
Amazon EC2 는 AWS 클라우드에서 확장 가능한 컴퓨팅 용량을 제공합니다. Amazon EC2를 사용하면 하드웨어 선투자할 필요가 없어 더 빠르게 애플리케이션을 개발하고 배포할 수 있습니다. Amazon EC2를 통해, 원하는 만큼 가상 서버를 구축하고 보안 및 네트워크 구성과 스토리지 관리가 가능합니다. 또한, Amazon EC2는 갑작스러운 트래픽 증가와 같은 변동 사항에도 신속하게 규모를 확장하거나 축소할 수 있어 서버 트래픽 예측 필요성이 줄어듭니다.

<p align="center"><img src="../images/amazon-ec2win-architecture.svg"></p>

아래의 순서 대로 실습을 진행하면서 웹 서버를 직접 구성합니다:

1. 키페어 생성하기

2. 웹 서버 인스턴스 생성하기

3. 윈도우 인스턴스에 접근하기

4. (옵션) 인스턴스 타입 변경하기

5. (옵션) Elastic IPs 사용하기

[Previous](./ec2-linux/5-ec2.md) | [Next](../10-ec2/ec2-windows/1-ec2.md)