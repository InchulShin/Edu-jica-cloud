# 로드밸런서 구성하기

## ELB(Elastic Load Balancing) 이해하기
[Elastic Load Balancing](https://aws.amazon.com/ko/elasticloadbalancing/?elb-whats-new.sort-by=item.additionalFields.postDateTime&elb-whats-new.sort-order=desc)은 들어오는 애플리케이션 트래픽을 Amazon EC2 인스턴스, 컨테이너, IP 주소, Lambda 함수, 가상 어플라이언스와 같은 여러 대상에 자동으로 분산시킵니다. Elastic Load Balancing은 단일 가용 영역 또는 여러 가용 영역에서 다양한 애플리케이션 부하를 처리할 수 있습니다. Elastic Load Balancing이 제공하는 네 가지 로드 밸런서는 모두 애플리케이션의 내결함성에 필요한 고가용성, 자동 조정, 강력한 보안을 갖추고 있습니다.

Application Load Balancer
Network Load Balancer
Gateway Load Balancer
Classic Load Balancer

![](./images/architecture.svg)

아래의 순서 대로 실습을 진행하면서 로드 밸런서를 직접 구성합니다.

[5-1.로드밸런서 생성하기](./5-1.create-elb.md)<br>

---

**다음** [5-1.로드밸런서 생성하기](./5-1.create-elb.md)