# 태그를 명시한 EC2 인스턴스 생성하기

## 태그를 명시한 EC2 인스턴스 생성하기
이번 실습에서는 두 개의 Amazon Linux 2 인스턴스를 실행할 것입니다. 하나는 개발 환경에서 사용되는 EC2 인스턴스이고 다른 하나는 운영 환경에서 사용되는 인스턴스라고 가정합니다. 이 두 인스턴스를 구분하기 위해 [tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) 를 사용할 것입니다.

![](../../images/two-ec2-instances.svg)

1. AWS 관리 콘솔에서 [EC2 콘솔](https://console.aws.amazon.com/ec2/v2/home) 에 접속합니다.

![](../../images/iam-1-01.png)

왼쪽 상단 메뉴에 있는 EC2 Dashboard를 클릭한 후, Launch instances 버튼을 클릭합니다.

![](../../images/ec2-lab-03.png)

2. Quick Start 메뉴에서 Free tier only를 클릭하고 가장 첫 번째에 있는 Amazon Linux 2 AMI 64-bit (x86)를 선택합니다.

![](../../images/ec2-lab-04.png)

3. Step 2에서 인스턴스 타입에서 t2.micro 인스턴스 사이즈를 선택한 후, Next: Configure Instance Details 버튼을 클릭합니다.

![](../../images/iam-1-ec2.png)

4. Step 3(Configure Instance Details), Step4(Add Storage) 항목은 기본 값을 유지합니다. Step 5에서 아래와 같이 키, 값을 추가합니다. 그 후, Review and Launch 버튼을 클릭합니다.

![](../../images/iam-1-ec2.png)

키 | 값
--- | ---
Name | prod-instance
Env | prod

5. Step 7(Review Instance Launch)에서 콘솔창 아래에 위치한 Launch 버튼을 클릭합니다. 팝업창이 나타나면 아래의 그림과 같이 설정한 후, Launch Instances 버튼을 클릭합니다.

![](../../images/iam-1-03.png)

6. 위의 작업을 통해, 운영 환경에서 사용하는 인스턴스가 실행됩니다. 그 다음으로는 개발 환경에서 사용하는 EC2 인스턴스를 생성해야 합니다. 위의 가이드(1번부터 5번)를 다시 수행하되, 4번은 아래와 같이 다르게 설정합니다.

![](../images/iam-1-04.png)

KEY | VALUE
--- | -----
Name | dev-instance
Env | dev

7. 왼쪽 사이드바 메뉴에서 instances를 클릭하면 두 개의 인스턴스를 확인할 수 있습니다. prod-instance의 체크 박스를 클릭하고 아래에 있는 Tags 탭을 클릭합니다. EC2 인스턴스의 태그 정보에 대한 자세한 내용을 파악할 수 있습니다.

![](../../images/iam-1-05.png)

잘하셨습니다! 여러 분은 각기 다른 리소스 태그가 있는 두개의 인스턴스를 배포하였습니다.

[Previous](../iam.md) | [Next](./2-iam.md)
